package il.ac.tau.cs.sw1.ex8.tfIdf;
import il.ac.tau.cs.sw1.ex8.histogram.HashMapHistogram;

import java.io.File;
import java.io.IOException;
import java.util.Comparator;
import java.util.Iterator;
import java.util.Map;
import java.util.HashMap;
import java.util.AbstractMap;
import java.util.Map.Entry;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;



/**************************************
 *  Add your code to this class !!!   *
 **************************************/

public class FileIndex {
	
	private boolean isInitialized = false;
	protected HashMap<String, HashMapHistogram> indexMap;
	protected HashMap<String, List<Entry<String, Double>>> significantWordMap;
	protected HashMap<String, Integer> docSizeMap; // indicate how many words are in a doc

	public FileIndex() {
		this.indexMap = new HashMap<String, HashMapHistogram>();
		this.significantWordMap = new HashMap<String, List<Map.Entry<String, Double>>>();
		this.docSizeMap = new HashMap<String, Integer>();
	}


	/*
	 * @pre: the directory is no empty, and contains only readable text files
	 * @pre: isInitialized() == false;
	 */
  	public void indexDirectory(String folderPath) throws IOException, FileIndexException { //Q1
		//This code iterates over all the files in the folder. add your code wherever is needed

		File folder = new File(folderPath);
		File[] listFiles = folder.listFiles();

		// creating indexMap
		for (File file : listFiles) { // for every file in the folder
			if (file.isFile()) {
				String fileName = file.getName();
				HashMapHistogram fileHistogram = new HashMapHistogram();
				List<String> tokens = FileUtils.readAllTokens(file);
				this.docSizeMap.put(fileName, tokens.size());
				fileHistogram.addAll(tokens);
				this.indexMap.put(fileName, fileHistogram);
			}
		}

			// filling significantWordMap
		Comparator<Entry<String, Double>> suitedComparator =
				Comparator.comparing(Map.Entry<String, Double>::getValue).reversed()
						.thenComparing(Map.Entry<String, Double>::getKey);

		for (String filename:indexMap.keySet()) {
			HashMapHistogram currHistogram = indexMap.get(filename);
			List<Map.Entry<String, Double>> currList = new ArrayList<>();
			Iterator<Map.Entry<String, Integer>> iterator = currHistogram.iterator();

			while (iterator.hasNext()) {
				String word = iterator.next().getKey();
				double val = getTFIDF(word, filename);
				currList.add(new AbstractMap.SimpleEntry<String, Double>(word, val));
			}

			currList.sort(suitedComparator);
			significantWordMap.put(filename, currList);

			/*
			Collections.sort(currList,
					Comparator.comparing((Map.Entry<String,Double> entry)-> entry.getValue()).reversed().
					thenComparing((Map.Entry<String, Double> entry)-> entry.getKey()));
			 */
		}
		isInitialized = true;
	}
	

	// Q2
  	
	/* @pre: isInitialized() */
	public int getCountInFile(String word, String fileName) throws FileIndexException {
		if (! this.indexMap.containsKey(fileName)) {
			throw new FileIndexException("File name doesn't found");
		}
		else {
			word = word.toLowerCase();
			HashMapHistogram fileHistogram = this.indexMap.get(fileName);
			return fileHistogram.getCountForItem(word);
		}
	}


	/* @pre: isInitialized() */
	public int getNumOfUniqueWordsInFile(String fileName) throws FileIndexException {
		if (! indexMap.containsKey(fileName))
			throw new FileIndexException("File name doesn't found");
		else
			return indexMap.get(fileName).getItemsSet().size();

	}


	/* @pre: isInitialized() */
	public int getNumOfFilesInIndex(){
		return this.indexMap.size();
	}

	
	/* @pre: isInitialized() */
	public double getTF(String word, String fileName) throws FileIndexException{ // Q3
		if (! indexMap.containsKey(fileName))
			throw new FileIndexException("File name doesn't found");
		else {
			return calcTF(getCountInFile(word, fileName), docSizeMap.get(fileName));
		}

	}


	/* @pre: isInitialized() 
	 * @pre: exist fileName such that getCountInFile(word) > 0*/
	public double getIDF(String word){ //Q4
		word = word.toLowerCase();
		int cnt = 0; // number of docs containing word
		for (HashMapHistogram histogram:indexMap.values()) {
			if (histogram.getCountForItem(word)>0)
				cnt+=1;
		}

		return calcIDF(getNumOfFilesInIndex(), cnt);
	}

	
	/*
	 * @pre: isInitialized()
	 * @pre: 0 < k <= getNumOfUniqueWordsInFile(fileName)
	 * @post: $ret.size() = k
	 * @post for i in (0,k-2):
	 * 		$ret[i].value >= $ret[i+1].value
	 */
	public List<Map.Entry<String, Double>> getTopKMostSignificantWords(String fileName, int k)
													throws FileIndexException{ //Q5
		return significantWordMap.get(fileName).subList(0, k);
	}


	/* @pre: isInitialized() */
	public double getCosineSimilarity(String fileName1, String fileName2) throws FileIndexException{ //Q6
		double numerator = 0;
		double denominatorA = 0;
		double denominatorB = 0;
		List<Map.Entry<String, Double>> A = significantWordMap.get(fileName1);
		List<Map.Entry<String, Double>> copyB = new LinkedList<>(significantWordMap.get(fileName2));
		//Collections.copy(copyB, significantWordMap.get(fileName2));

		for (Map.Entry<String, Double> entryA:A) {
			if (! (getCountInFile(entryA.getKey(), fileName2) > 0)) {
				continue;
			}

			else {
				Double eqvWordB = 0.0;
				for (Map.Entry<String, Double> entryB:copyB) {
					if (entryA.getKey().equals(entryB.getKey())) {
						eqvWordB = entryB.getValue();
						copyB.remove(entryB);
						break;
					}
				}

				numerator += entryA.getValue() * eqvWordB;
				denominatorA += Math.pow(entryA.getValue(), 2);
				denominatorB += Math.pow(eqvWordB, 2);
			}

		}

		double cosSim = numerator/(Math.sqrt(denominatorA*denominatorB));
		return cosSim;
	}


	/*
	 * @pre: isInitialized()
	 * @pre: 0 < k <= getNumOfFilesInIndex()-1
	 * @post: $ret.size() = k
	 * @post for i in (0,k-2):
	 * 		$ret[i].value >= $ret[i+1].value
	 */
	public List<Entry<String, Double>> getTopKClosestDocuments(String fileName, int k)
			throws FileIndexException{ //Q6

		List<Map.Entry<String, Double>> list = new ArrayList<>();
		for(String file_name:indexMap.keySet()) {
			if (file_name.equals(fileName))
				continue; //don't insert the file name itself
			double val = getCosineSimilarity(fileName, file_name);
			list.add(new AbstractMap.SimpleEntry<String, Double>(file_name,val));
		}

		List<Map.Entry<String,Double>> sublist = list.subList(0, k);
		sublist.sort((o1, o2) -> o2.getValue().compareTo(o1.getValue()));
		return sublist;
	}


	//add private methods here, if needed

	
	/*************************************************************/
	/********************* Don't change this ********************/
	/*************************************************************/
	
	public boolean isInitialized(){
		return this.isInitialized;
	}
	
	/* @pre: exist fileName such that getCountInFile(word) > 0*/
	public double getTFIDF(String word, String fileName) throws FileIndexException{
		return this.getTF(word, fileName)*this.getIDF(word);
	}
	
	private static double calcTF(int repetitionsForWord, int numOfWordsInDoc){
		return (double)repetitionsForWord/numOfWordsInDoc;
	}
	
	private static double calcIDF(int numOfDocs, int numOfDocsContainingWord){
		return Math.log((double)numOfDocs/numOfDocsContainingWord);
	}
	
}

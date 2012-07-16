import java.util.ArrayList;
import java.util.Set;


public class main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		//1 connect with db
		//2 get data from db,arraylist<Document>,set<Lexical>
		//3 compute the weight
		//4 write back to db
	}

	void compute(ArrayList<Document> doc,Set<Lexical> word,float a,float b)
	{
		int doc_len,list_len,pk;
		float avg_len,sum = (float) 0.0;
		for (Lexical tmp:word)
		{
			sum += tmp.length();
		}
		avg_len = sum / word.size();
				
		list_len = doc.size();
		for (int i = 0;i < list_len;i++)
		{
			doc_len = doc.get(i).length();
			pk = doc.get(i).get_pk();
			for (Lexical tmp:word)
			{
				float weight = (float) 0.0;
				float weight_p = tmp.get_pos(pk) / doc.get(i).get_size();
				if (tmp.get_times(pk) != -1)
				{ 
					weight = (float) (a * (1 + Logarithm.log(tmp.get_times(pk), 2) * Logarithm.log(doc.size() / tmp.show_times(), 2) * weight_p) / doc_len + b * (tmp.length() / avg_len) * weight_p);
					tmp.set_wight(pk, weight);
				}
			}
		}
	}
	
}

class Logarithm {
	static public double log(double value, double base)
	 {
		return Math.log(value) / Math.log(base);
	}
}

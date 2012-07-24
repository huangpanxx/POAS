import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;


public class main {

	/**
	 * @param args
	 * @throws SQLException 
	 * @throws IOException 
	 */
	public static void main(String[] args) throws SQLException, IOException {
		// TODO Auto-generated method stub

		ArrayList<Document> doc = new ArrayList<Document>();
		HashSet<Lexical> word = new HashSet<Lexical>();
		ArrayList<String> stop_word = new ArrayList<String>();
		float a = (float) 0.8,b = (float) 0.2;
		
		//get data from files,arraylist<Document>,set<Lexical> and stop_word
		input_stop(stop_word);
		input(doc,word,stop_word);

		//compute the weight
		compute(doc,word,a,b);
//		for (Lexical tmp:word)
//			tmp.print();
//		for (Document tmp:doc)
//			tmp.print();
	
		
		//write back to db
		Connection conn = connect_db();
		write_back(conn,doc,word);
		conn.close();
	}

	private static void input_stop(ArrayList<String> stop_word) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("src/stop.txt")));
		String line;
		while ((line = br.readLine()) != null)
			stop_word.add(line.toString());
	}

	static Connection connect_db()
    {
    	String driver = "com.mysql.jdbc.Driver";
    	String url = "jdbc:mysql://10.250.62.6:3306/hot";
    	String user = "longruiliu";
    	String passwd = "liurui";
    	Connection conn = null;
    	try{
    		Class.forName(driver);
    		conn = DriverManager.getConnection(url,user,passwd);
    		if (!conn.isClosed())
    		{
    			System.out.println("Succeeded connecting to the Database!");
    			return conn;
    		}
    		else
    			System.out.println("Connecting Database error!");
    	}catch(Exception e)
    	{
    		e.printStackTrace();
    	}
    	return conn;
    }
	
	static void input(ArrayList<Document> doc,HashSet<Lexical> word, ArrayList<String> stop_word) throws IOException
	{
		File file = new File("src/test/");
		File[] file_list = file.listFiles();
		for (int i = 1;i <= file_list.length;i++)
		{
			 BufferedReader fin = new BufferedReader(new FileReader(file_list[i - 1]));  
			 Document doc_tmp = new Document(i,"news");
		     String line = fin.readLine();
		     int file_length = 0,file_size = 0;
		     while(line != null)
		     {  
		    	 StringTokenizer str = new StringTokenizer(line, " ");  
		    	 while (str.hasMoreTokens())
		    	 {
		    		 String tmp = str.nextToken();
		    		 String delims = "/";
		    		 String[] tokens = tmp.split(delims);
		    		 
		    		 //don't use the words in the stop words;
		    		 if (in_stop(tokens[0],stop_word))
		    			 continue;
		    		 
		    		 //don't use the words which part_of_speech are p,w,c,u.
		    		 if (tokens[1].indexOf('w') == -1&&tokens[1].indexOf('p') == -1&&
		    				 tokens[1].indexOf('c') == -1&&tokens[1].indexOf('u') == -1)
		    		 {
		    			 Lexical word_tmp = new Lexical(tokens[0],tokens[1]);
		    			 int mark = 0;   //if mark = 0,this word isn't in the set;otherwise,in the set
		    			 
		    			 if (word != null)
		    			 {
		    				 for (Lexical it:word)
			    			 {
			    				//find the word in the set
			    				 if (it.equals(word_tmp))
			    				 {
			    					//whether the word has shown in this article.
			    					 if (it.get_pos(i) == -1)
			    						 it.set_pos(i, file_size);
			    					 it.add_times(i);
			    					 mark = 1;
			    					 break;
			    				 }
			    			 }
		    			 }
		    			 if (mark == 0)
		    			 {
		    				 word_tmp.add_times(i);
		    				 word_tmp.set_pos(i, file_size);
		    				 word.add(word_tmp);
		    			 }
		    			 file_size++;
			    		 file_length += tokens[0].length();
		    		 }
		    	 }
		         line = fin.readLine();  
		      } 
		     doc_tmp.set_len(file_length);
		     doc_tmp.set_size(file_size);
		     doc.add(doc_tmp);
		     fin.close();  
		}
	}

	private static boolean in_stop(String string, ArrayList<String> stop_word) {
		// TODO Auto-generated method stub
		for (String tmp:stop_word)
			if (tmp.equals(string))
				return true;
		return false;
	}

	static void compute(ArrayList<Document> doc,HashSet<Lexical> word,float a,float b)
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
				float weight_p = (float) (1.0 * tmp.get_pos(pk) / doc.get(i).get_size());
				if (tmp.get_times(pk) != -1)
				{ 
					weight = (float) (a * (1 + Logarithm.log(tmp.get_times(pk), 2) * Logarithm.log(doc.size() / tmp.show_times(), 2) * tmp.get_part()) / doc_len + b * (tmp.length() / avg_len) * weight_p);
					tmp.set_wight(pk, weight);
				}
			}
		}
	}
	
	static void write_back(Connection conn,ArrayList<Document> doc,HashSet<Lexical> word) throws SQLException
	{
		Statement statement = conn.createStatement();
		//write to hot_doc
		for (Document tmp:doc)
		{
			int pk = tmp.get_pk();
			int length = tmp.length();
			int size = tmp.get_size();
			String s_url = tmp.get_url();
			String field = tmp.get_field(); 
			
			statement.executeUpdate("insert into hot_doc (id,url,length,size,field,date) values ('"+pk+"','"+s_url+"','"+length+"','"+size+"','"+field+"',now())");
		}
		
		//write to hot_lexical
		for (Lexical tmp:word)
		{
			String value = tmp.value();
			int length = tmp.length();
			String part_of_speech = tmp.part();
			float weight = tmp.total_weight();
			
			statement.executeUpdate("insert into hot_lexical (value,length,part_of_speech,total_weight,date) values ('"+value+"','"+length+"','"+part_of_speech+"','"+weight+"',now())");
		}
		
		//write to hot_lex_doc
		for (Lexical tmp:word)
		{
			String value = tmp.value();
			int lexical_id = 0;
			ResultSet rs = statement.executeQuery("select id from hot_lexical where value = '"+value+"'");
			while (rs.next())
				lexical_id = rs.getInt("id");
			for (Integer pk:tmp.get_map().keySet())
			{
				int times = tmp.get_times(pk);
				int first_pos = tmp.get_pos(pk);
				
				statement.executeUpdate("insert into hot_lex_doc (Lexical_id,Doc_id,times,first_pos,date) values ('"+lexical_id+"','"+pk+"','"+times+"','"+first_pos+"',now())");
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

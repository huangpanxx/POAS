
public class Document 
{
	private int pk;                                           //the primary key of this document
	private int length;                                       //the length of this document
	private int size;                                         //the lexical number of document
	private String head;                                      //head of the document
	private String s_url;                                     //the url of this document
	private String field;                                     //the type of document like news,weibo,blog......
	
	Document(int pk_in,String head_in,String field_in)
	{
		pk = pk_in;
		head = head_in;
		field = field_in;
	}
	
	public int get_pk()
	{
		return pk;
	}
	
	public void set_len(int len)
	{
		length = len;
	}
	
	public int length()
	{
		return length;
	}
	
	public void set_size(int tmp)
	{
		size = tmp;
	}
	
	public int get_size()
	{
		return size;
	}
	
	public String get_head()
	{
		return head;
	}
	
	public String get_url()
	{
		return s_url;
	}
	
	public String get_field()
	{
		return field;
	}
}

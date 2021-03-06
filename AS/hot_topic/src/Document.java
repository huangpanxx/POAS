
public class Document 
{
	private int pk;                                           //the primary key of this document
	private int length;                                       //the length of this document
	private int size;                                         //the lexical number of document
	
	Document(int pk_in)
	{
		pk = pk_in;
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
	
	
	public void print()
	{
		System.out.print(pk);
		System.out.print("\t");
		System.out.print(length);
		System.out.print("\t");
		System.out.print(size);
		System.out.print("\n");
	}
}

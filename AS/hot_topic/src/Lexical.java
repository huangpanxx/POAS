import java.util.HashMap;
import java.util.Map;

public class Lexical 
{
	private String value;                                  //word's value
	private int length;                                    //the length of the word
	private String part_of_speech;
	private Map<Integer, Integer> m_times = new HashMap<Integer,Integer>();                 //how many times shown in specific document
	private Map<Integer,Integer> m_pos = new HashMap<Integer,Integer>();                   //position that the word first shown in specific document
	private Map<Integer,Float> m_weight = new HashMap<Integer,Float>();                   //word's weight in specfic document
	
	public Lexical(String name,String part)
	{
		value = name;
		part_of_speech = part;
		length = name.length();
	}
	
	public String value()
	{
		return value;
	}
	
	public void add_times(int pk)
	{
		if (m_times != null&&m_times.containsKey(pk))
		{
			int tmp = m_times.get(pk);
			tmp++;
			m_times.put(pk, tmp);
		}
		else
			m_times.put(pk, 1);
	}
	
	public int get_times(int pk)
	{
		if (m_pos != null&&m_pos.containsKey(pk))
			return m_times.get(pk);
		else
			return -1;
	}
	
	public int length()
	{
		return length;
	}
	
	public void set_pos(int pk,int pos)
	{
		m_pos.put(pk, pos);
	}
	
	public int get_pos(int pk)
	{
		if (m_pos != null&&m_pos.containsKey(pk))
			return m_pos.get(pk);
		else
			return -1;
	}
	
	public void set_wight(int pk,Float wt)
	{
		m_weight.put(pk, wt);
	}
	
	public float get_weight(int pk)
	{
		if (m_weight != null&&m_weight.containsKey(pk))
			return m_weight.get(pk);
		else
			return -1;
	}
	
	public float total_weight()
	{
		float max = (float) 0.0;
		float sum = (float) 0.0;
		for (int tmp:m_weight.keySet())
			if (m_weight.get(tmp) > max)
				max = m_weight.get(tmp);
		for (int tmp:m_weight.keySet())
			sum += m_weight.get(tmp);
		return sum / max;
	}
	
	public float get_part()
	{
		if (part_of_speech.indexOf('n') != -1)
			return 2;
		else if (part_of_speech.indexOf('v') != -1)
			return (float) 1.5;
		else
			return 1;
	}
	
	public int show_times()
	{
		return m_pos.size();
	}
	
	public Map<Integer,Integer> get_map()
	{
		return m_times;
	}
	
	public int hashcode()
	{
		return value.hashCode();
	}
	
	public Boolean equals(Lexical tmp)
	{
		if (tmp.value().equals(this.value))
			return true;
		return false;
	}
	
	public void print()
	{
		System.out.print(value);
		System.out.print(" ");
		System.out.print(length);
		System.out.print(" ");
		System.out.print(part_of_speech);
		System.out.print("\n");
		for (int tmp:m_times.keySet())
		{
			System.out.print(tmp);
			System.out.print(" ");
			System.out.print(m_times.get(tmp));
			System.out.print(" ");
			System.out.print(m_pos.get(tmp));
			System.out.print(" ");
			System.out.print(m_weight.get(tmp));
			System.out.print("\t");
		}
		System.out.println();
	}

	public String part() 
	{
		return part_of_speech;
	}
}

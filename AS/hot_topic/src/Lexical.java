import java.util.Map;

public class Lexical 
{
	private String value;                                  //word's value
	private int length;                                    //the length of the word
	private String part_of_speech;
	private Map<Integer, Integer> m_times;                 //how many times shown in specific document
	private Map<Integer,Integer> m_pos;                    //position that the word first shown in specific document
	private Map<Integer,Float> m_weight;                   //word's weight in specfic document
	
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
		if (m_times.containsKey(pk))
		{
			int tmp = m_times.get(pk);
			tmp++;
			m_times.put(pk, tmp);
		}
		else
		{
			m_times.put(pk, 0);
		}
	}
	
	public int get_times(int pk)
	{
		if (m_pos.containsKey(pk))
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
		if (m_pos.containsKey(pk))
			return m_pos.get(pk);
		else
			return -1;
	}
	
	public void set_wight(int pk,Float wt)
	{
		m_weight.put(pk, wt);
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
	
	public String get_part()
	{
		return part_of_speech;
	}
	
	public int show_times()
	{
		return m_pos.size();
	}
}

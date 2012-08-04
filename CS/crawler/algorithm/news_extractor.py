#coding:utf8

import urllib2
import re
from crawler.utils.charset import decodeHtml
from .readability import Readability



#提取纯文本
def preProcess(html):
	#去除无用信息
	html = re.sub(r"(?s)\s*<!DOCTYPE.*?>", '', html)
	html = re.sub(r"(?s)\s*<!--.*?-->", '', html)
	html = re.sub(r"(?s)\s*<script.*?>.*?</script>", '', html)
	html = re.sub(r"(?s)\s*<style.*?>.*?</style>", '', html)
	html = re.sub(r"&.{2,5};|&#.{2,5};", '', html)
	html = re.sub(r"(?s)\s<img.*?/>", '', html)
	html = re.sub(r"(?s)\s<textarea.*?>.*?</textarea>",'',html)

	#段落处理(缩进)
	lines = re.split(r'(?i)\s*<p.*?>', html) #p pre
	lines = [i for i in lines if i] #去除 None

	tags = ('span', 'a', 'strong') #不换行的标签

	#段内处理
	for i in range(len(lines)):
		value = lines[i]
		for tag in tags:
			value = re.sub(r"(?s)\s*<%s .*?>\s*" % (tag,), '', value) #不换行

		value = re.sub(r"(?is)</.*?>\s*", '', value) #末标签不换行
		value = re.sub(r"(?is)<.*?>\s*", '\n', value) #首标签换行
		lines[i] = unicode(value,'utf-8','ignore').strip().encode('utf-8')

	html = '\r\n\t'.join([i for i in lines]) #<p>标签换行空格

	return html

#依据行分布提取正文
def getText(html, blocksWidth=2, threshold=150):

	_lines = html.split('\n')

	lines = []

	#去除空白行
	for i in _lines:
		if not i.strip():
			i = ''
		lines.append(i)
	
	indexDistribution = []

	for i in range(len(lines) - blocksWidth):
		wordsNum = 0
		for j in range(i, i + blocksWidth):
			wordsNum += len(lines[j])
		indexDistribution.append(wordsNum)

	start = -1; end = -1
	boolstart = False; boolend = False
	text = ''

	for i in range(len(indexDistribution) - 4):
		if(indexDistribution[i] > threshold and (not boolstart)):
			b1 = (indexDistribution[i + 1] != 0)
			b2 = (indexDistribution[i + 2] != 0)
			b3 = (indexDistribution[i + 3] != 0)
			if b1 or b2 or b3:
				boolstart = True
				start = i
				continue
	
		if boolstart:
			b1 = (indexDistribution[i] == 0)
			b2 = (indexDistribution[i + 1] == 0)
			if b1 or b2:
				end = i
				boolend = True
		
		if boolend:
			tmp = []
			for i in range(start, end + 1):
				s = lines[i]
				if len(s) < 5:
					continue
				if ('Copyright' in s) or ('版权' in s):
					continue
				tmp.append(s + '\n')

			boolstart = boolend = False

			_str = ''.join(tmp)

			ls = _str.splitlines()
			start = -1
			for i in range(len(ls)):
				if ls[i].startswith('\t'):
					start = i
					break
			
			end = -1
			for i in range(len(ls)-1,0,-1):
				if ls[i].startswith('\t'):
					end = i
					break
			
			if start==-1:
				_str = ''
			else:
				_str = '\r\n'.join(ls[start:end+1])
	
			if len(_str) > len(text):
				text = _str

	return text

def datetimeprocessor1(text):
	re.search()
	pass

def getDateTime(text):
	patterns = ( 
			r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(\s+\d{2}:\d{2})?' ,
			r'(?P<year>\d{4})年(?P<month>\d{2})月(?P<day>\d{2})日(\s+\d{2}:\d{2})?'   ,
			r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})(\s+\d{2}:\d{2})?',
			)
	for p in patterns:
		m = re.search(p, text)
		if m:
			group = m.group
			year = group('year')
			month = group('month')
			day = group('day')
			return '%s-%s-%s' % (year,month,day)
	return None

def getTitle(html):
	m = re.search('<title>(.*)</title>', html)
	if m:
		return m.group(1)
	return None

def getCommentNbr(text):
	patterns = (
			r'(\d+)人参与',
			r'(\d+)人评论',)
	for p in patterns:
		m = re.search(p, text)
		if m:
			return m.group(1)
	return None

def parseHtml(html, blocksWidth=3, threshold=100):
	r = Readability(html,'')
	#title = getTitle(html)
	html = preProcess(html)
	commentNbr = getCommentNbr(html)
	datetime = getDateTime(html)
	title = r.title.encode('utf8')
	text = r.content.encode('utf8')
	
	#text = getText(html, blocksWidth, threshold)
	return {'title':title,
			'datetime':datetime,
			'text':text,
			'commentNbr':commentNbr}
	

if __name__ == '__main__':
	def getHtml(url):
		opener = urllib2.urlopen(url)
		data = opener.read()
		html = decodeHtml(data)
		return html
		

	def printDict(dic):
		for key, value in dic.items():
			print '%s:%s' % (key, value)
		
	def writeFile(path, text):
		f = open(path, 'w')
		f.write(text)
		f.close()

	#url = 'http://ent.qq.com/a/20100417/000119.htm'
	#url = 'http://mil.news.sina.com.cn/2012-07-11/1056695377.html'
	#url = 'http://www.top81.com.cn/2012/0711/3639.htm'
	#url = 'http://club.mil.news.sina.com.cn/viewthread.php?tid=508479'
	#url = 'http://phtv.ifeng.com/program/news/detail_2012_07/11/15940998_0.shtml'
	#url = 'http://lssnail.tk'
	#url = 'http://news.sina.com.cn/c/2012-07-10/213524748852.shtml'
	url = 'http://news.ifeng.com/mainland/special/diaoyudaozhengduan/content-3/detail_2012_07/09/15885116_0.shtml'
	
	html = getHtml(url)
	info = parseHtml(html)
	printDict(info)
	

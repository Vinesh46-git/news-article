<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Type &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">IPython 7.19.0 -- An enhanced Interactive Python.</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">1</span><span style=" color:#00ff00;">]:</span> !pip install Scrapy==1.0.3pip freeze &gt; requirements.txt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">ERROR: Could not find a version that satisfies the requirement Scrapy==1.0.3pip (from versions: 0.7, 0.8, 0.9, 0.10.4.2364, 0.12.0.2550, 0.14.1, 0.14.2, 0.14.3, 0.14.4, 0.16.0, 0.16.1, 0.16.2, 0.16.3, 0.16.4, 0.16.5, 0.18.0, 0.18.1, 0.18.2, 0.18.3, 0.18.4, 0.20.0, 0.20.1, 0.20.2, 0.22.0, 0.22.1, 0.22.2, 0.24.0, 0.24.1, 0.24.2, 0.24.3, 0.24.4, 0.24.5, 0.24.6, 1.0.0rc1, 1.0.0rc2, 1.0.0rc3, 1.0.0, 1.0.1, 1.0.2, 1.0.3, 1.0.4, 1.0.5, 1.0.6, 1.0.7, 1.1.0rc1, 1.1.0rc2, 1.1.0rc3, 1.1.0rc4, 1.1.0, 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.2.0, 1.2.1, 1.2.2, 1.2.3, 1.3.0, 1.3.1, 1.3.2, 1.3.3, 1.4.0, 1.5.0, 1.5.1, 1.5.2, 1.6.0, 1.7.0, 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.8.0, 2.0.0, 2.0.1, 2.1.0, 2.2.0, 2.2.1, 2.3.0, 2.4.0, 2.4.1, 2.5.0)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">ERROR: No matching distribution found for Scrapy==1.0.3pip</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">2</span><span style=" color:#00ff00;">]:</span> !pip install Scrapy==1.0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting Scrapy==1.0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading Scrapy-1.0.3.tar.gz (948 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting Twisted&gt;=10.0.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading Twisted-21.2.0-py3-none-any.whl (3.1 MB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting w3lib&gt;=1.8.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading w3lib-1.22.0-py2.py3-none-any.whl (20 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting queuelib</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading queuelib-1.6.1-py2.py3-none-any.whl (12 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: lxml in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from Scrapy==1.0.3) (4.6.1)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: pyOpenSSL in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from Scrapy==1.0.3) (19.1.0)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting cssselect&gt;=0.9</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading cssselect-1.1.0-py2.py3-none-any.whl (16 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: six&gt;=1.5.2 in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from Scrapy==1.0.3) (1.15.0)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting service_identity</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading service_identity-21.1.0-py2.py3-none-any.whl (12 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting Automat&gt;=0.8.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading Automat-20.2.0-py2.py3-none-any.whl (31 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting hyperlink&gt;=17.1.1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading hyperlink-21.0.0-py2.py3-none-any.whl (74 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting incremental&gt;=16.10.1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading incremental-21.3.0-py2.py3-none-any.whl (15 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting twisted-iocpsupport~=1.0.0; platform_system == &quot;Windows&quot;</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading twisted_iocpsupport-1.0.1-cp38-cp38-win_amd64.whl (45 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: attrs&gt;=19.2.0 in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from Twisted&gt;=10.0.0-&gt;Scrapy==1.0.3) (20.3.0)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting constantly&gt;=15.1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading constantly-15.1.0-py2.py3-none-any.whl (7.9 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: zope.interface&gt;=4.4.2 in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from Twisted&gt;=10.0.0-&gt;Scrapy==1.0.3) (5.1.2)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: cryptography&gt;=2.8 in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from pyOpenSSL-&gt;Scrapy==1.0.3) (3.1.1)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: pyasn1-modules in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from service_identity-&gt;Scrapy==1.0.3) (0.2.8)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: pyasn1 in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from service_identity-&gt;Scrapy==1.0.3) (0.4.8)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: idna&gt;=2.5 in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from hyperlink&gt;=17.1.1-&gt;Twisted&gt;=10.0.0-&gt;Scrapy==1.0.3) (2.10)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: setuptools in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from zope.interface&gt;=4.4.2-&gt;Twisted&gt;=10.0.0-&gt;Scrapy==1.0.3) (50.3.1.post20201107)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: cffi!=1.11.3,&gt;=1.8 in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from cryptography&gt;=2.8-&gt;pyOpenSSL-&gt;Scrapy==1.0.3) (1.14.3)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: pycparser in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (from cffi!=1.11.3,&gt;=1.8-&gt;cryptography&gt;=2.8-&gt;pyOpenSSL-&gt;Scrapy==1.0.3) (2.20)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Building wheels for collected packages: Scrapy</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Building wheel for Scrapy (setup.py): started</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Building wheel for Scrapy (setup.py): finished with status 'done'</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Created wheel for Scrapy: filename=Scrapy-1.0.3-py3-none-any.whl size=291190 sha256=351c6aa5ae7c823265b690ad0e4c81fb27baaf6ce10bfd076efd7a3d0fac8837</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Stored in directory: c:\users\kittu vinny\appdata\local\pip\cache\wheels\33\0e\4a\046a302ab60013c29d9a4843382f96fa9dc07fab0cc50b18e4</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Successfully built Scrapy</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Installing collected packages: Automat, hyperlink, incremental, twisted-iocpsupport, constantly, Twisted, w3lib, queuelib, cssselect, service-identity, Scrapy</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Successfully installed Automat-20.2.0 Scrapy-1.0.3 Twisted-21.2.0 constantly-15.1.0 cssselect-1.1.0 hyperlink-21.0.0 incremental-21.3.0 queuelib-1.6.1 service-identity-21.1.0 twisted-iocpsupport-1.0.1 w3lib-1.22.0</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">3</span><span style=" color:#00ff00;">]:</span> !pip freeze &gt; requirements.txt</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">4</span><span style=" color:#00ff00;">]:</span> import scrapy</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">5</span><span style=" color:#00ff00;">]:</span> !pip install pymongo</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Collecting pymongo</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  Downloading pymongo-3.11.4-cp38-cp38-win_amd64.whl (383 kB)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Installing collected packages: pymongo</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Successfully installed pymongo-3.11.4</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">6</span><span style=" color:#00ff00;">]:</span> !pip freeze &gt; requirements.txt</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">7</span><span style=" color:#00ff00;">]:</span> !pip install pymongo</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Requirement already satisfied: pymongo in c:\users\kittu vinny\anaconda3\anaconda\lib\site-packages (3.11.4)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">8</span><span style=" color:#00ff00;">]:</span> </p></body></html>
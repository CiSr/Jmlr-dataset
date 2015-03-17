AttributeList.txt

     The final output is in the format:
					Author 1..N:Titles of his research papers.

     The dataset corresponds to dblp - jmlr: http://www.informatik.uni-trier.de/~%20LEY/db/journals/jmlr/index.html

     There are 1158 papers along with their corresponding authors and titles.

Extraction of urls:

    The urls for the different authors are extracted using the grep command in the file url_extract.txt

Extraction of XML files:
 
     Each paper will correspond to an url and each url will contain an XML file in the format as follows:
    
     <?xml version="Version number"?>
     <dblp>
     <article key="A Key Id" mdate="Making date">
     <author>Name of Author_1</author>
     <author>Name of Author_2</author>
     <title>Title of the paper</title>
     <pages>Total number of pages</pages>
     <year>Published year</year>
     <volume>Specified volume</volume>
     <journal>Name of the journal</journal>
     <ee>url of the abstract</ee>
     <url>url of the research paper</url>
     </article>
     </dblp>

     Similarly there are XML files for the urls of all the 1158 papers.
     
     These XML files are extracted using the java code xml_downloader.java

     The XML for different urls are stored in different files as output1, output2, etc... in the folder xml_files.txt (1159 files)


     The file finalDict.py contains the following information:
	
     These 1159 o*.xml are converted  into a dictionary in python using xmltodict command.
	
     The tags like author and title are alone extracted.

     Finally we store the author and his associated research papers into the dictionary. 


       Note:(*) represents  0 or many characters
   






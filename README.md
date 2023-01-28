# learning-and-research-accelerator

Tool framework for Symbiotic Intelligence - with the goal of facilitating learning and research in both man and machine.


## End Design Goal: 

Create a tool framework around the "principle of emergence"* to enable the "symbiotic relationship between man and machine"* to be "more than the sum of its parts" - or Symbiotic Intelligence - to improve accelleration of productivity, reduction of error, increased output, faster decision management with better information, and more.  

### Driving purpose: 

Currently struggling with Aphasia, ADHD, dislexia, Fibromyalgia and more - hope this kind of tool can help those with these and other kinds of "disabilities/abilities/superpowers", in their quest to learn, research, and fit into, or back into, society.

Absolutely hoping it'll help more than just me, and more than those stated above!

### References for "principle of emergence"
  * https://www.sebokwiki.org/wiki/Emergence ['As defined by Checkland, emergence is “the principle that entities exhibit properties which are meaningful only when attributed to the whole, not to its parts.” ' (Checkland 1999, 314).]

  * Checkland, P. 1999. Systems Thinking, Systems Practice. New York, NY, USA: John Wiley & Sons. 

  * [The sky’s the limit: why together we’re greater than the sum of our parts](https://www.theguardian.com/books/2020/feb/15/the-skys-the-limit-why-together-we-are-greater-than-the-sum-of-our-parts)

  * [Team: are you more than the sum of your parts?](https://medium.com/corporate-strategy/team-are-you-more-than-the-sum-of-your-parts-db9e98f9b836)

### Reference for "Symbiotic relationship between man and machine"
“Symbiotic relationship of Man and Machine in Space Colonization”, in the proceedings of Space Technology and Applications International Forum-2007, Roy Nielsen, AIP Conference Proceedings 880, Melvile, New York, 2007 pp. 888-896

 
## Potential other projects to pull into this project, or attempt to integrate with, or make a "Alara" plugin for:

The intent is for the App to provide a front end, glue logic, apis, plugin environment, pulling in a variety of search algorithms, libraries, frameworks and applications to facilitate accelleration of research and learning.


### Scraping
Integrated | Library/App/Framework | link
--- | --- | ---
not yet | scrapy - network/web scraping |  https://www.datacamp.com/tutorial/making-web-crawlers-scrapy-python , https://github.com/scrapy/scrapy

### Searching
Integrated | Library/App/Framework | link
--- | --- | ---
not yet | dynamic programming based search algorithms | many, one specific project -  https://github.com/junegunn/fzf
not yet | fzf | https://github.com/andreax79/pzp
not yet | snowball | https://snowballstem.org/


### Model info
Integrated | Library/App/Framework | link
--- | --- | ---
not yet | Zotero | https://github.com/zotero/zotero
not yet | ck/cm frameworks | https://ck.readthedocs.io/en/latest/src/introduction.html , https://github.com/mlcommons/ck


### View Related

Integrated | Library/App/Framework | link
--- | --- | ---
not yet | Use this static framework to create a dynamic search environment, that collects, tracks and houses biblographical information on searches in zotero - perhaps more in the future... | https://github.com/whiskyechobravo/kerko
not yet | mistletoe - mardown/html parser | https://github.com/miyuchina/mistletoe 
not yet | magicgui - app | https://github.com/pyapp-kit/magicgui
not yet | flask - web server (dev version - use latest stable) | https://flask.palletsprojects.com/en/latest/ </p> https://pythonbasics.org/what-is-flask-python/ </p> https://pythongeeks.org/python-flask-introduction/ </p> https://www.leniolabs.com/software-development/2023/01/26/Create-and-host-your-web-app-with-Python-and-Flask-Part2/


### Plugin framework references
Integrated | Library/App/Framework | link
--- | --- | ---
not yet | npe2 (or similar plugin framework - but this is already in python)  | https://github.com/napari/npe2


### Frameworks to integrate into the project
Integrated | Library/App/Framework | link
--- | --- | ---
not yet | ck - Collective Knowledge | https://www.cknowledge.org/ </p> https://github.com/mlcommons/ck </p> https://ck.readthedocs.io/en/latest/src/introduction.html </p> https://github.com/topics/collective-knowledge </p> https://royalsocietypublishing.org/doi/10.1098/rsta.2020.0211 </p> https://ieeexplore.ieee.org/document/7459430?arnumber=7459430 </p> https://awesomeopensource.com/projects/collective-knowledge/portable-workflows/python </p> https://www.youtube.com/watch?v=IJQ-PpSU1kY </p> https://www.youtube.com/watch?v=7zpeIVwICa4 </p> https://www.youtube.com/watch?v=pk231d_4esI </p> https://www.youtube.com/playlist?list=PL_O7lvvJGLbg54GdWTqcoDHzByQhs2RMX


### Modeling languages/info
Integrated | Library/App/Framework | link
--- | --- | ---
not yet | plantUML | https://github.com/plantuml
not yet | mermaid | https://github.com/mermaid-js/mermaid
not yet | kroki | https://github.com/yuzutech/kroki
not yet | drawio | https://github.com/jgraph/drawio
not yet | vym | https://github.com/insilmaril/vym


### Apps to integrate with
Integrated | Library/App/Framework | link
--- | --- | ---
not yet | discord | https://github.com/discord
not yet | slack | https://github.com/slackapi/python-slack-sdk
not yet | atlassian products | https://www.atlassian.com/



##  Use Cases

### Miminum viable product:

1. Kerloapp as default - just read a zotero db and display (local or web)
2. Scrape web page for ris/zot related info and store in zot db (local or web)
3. Scrape PDF for ris/zont related info and store in zot db (local or web)
4. scholar.google.com, search for info, collect ris, put in zot db (local or web)
5. Dynamicaly generate kerkoapp page based on in-memory ris/zot model info
6. dynamic templates for kerkoapp generation

### Future possible use cases, may help guide the front end of the design process

7. collect ris+ from web page put in zot db (local or remote)
8. Integrate snowball and fzf into kerkoapp type templates (searching algorithms)

## Possible project phases - or sprints

### one

Design - how could it all go together - patterns, processes, etc.  Partway done...

-- only a sprint or two - otherwise, one would be forever in this phase...

consider services in terms of microservices - 
* views possibly implemented via microservice, or magicgui type app
* use case defined as a microservice



### two

Start prototyping use of initial collection as proposed in phase one

Likely a several phases, for each of alpha, beta & gold, reaching 1.0

To reach 1.0, the following must be met - use cases on through five, with the following if possible

* the following must be integrated into an MVC type pattern, described in the design directory
- [ ] use case one implemented
- [ ] use case two implemented
- [ ] use case three implemented
- [ ] use case four implemented
- [ ] use case five implemented
- [ ] use case six implemented
- [ ] Bibliography database integration - if possible, Zotero - open source bibliography database software and plugins
- [ ] Interface to Bibliography database, similar to Kerko - static website based on a zotero database
- [ ] Network/web searching capability - scapy - network/web scraping
- [ ] Dynamic programming based search/sort, possibly based on fzf - awesome fast searching..
- [ ] Plugin framework, possibly based on npe2 - if not integrating npe2, a similarly functioning plugin structure for 1.0
- [ ] Views completely divorced from models, controller, any internals - easily swapable via interface definition

The above will be bound with a front end, based on, or similar to Kerko, except be a dynamically generated page based on search criteria similar to google's search criteria.  Eventually many search engines will be usable or their functionality used/leveraged.  First pass search engines:

- [ ] google.com
- [ ] scholar.google.com

stretch goals:
- [ ] images.google.com
- [ ] news.google.com
- [ ] NOAA weather search
- [ ] weather underground search

### three

- [ ]  
- [ ]  
- [ ]  
- [ ]  
- [ ]  
- [ ]  
- [ ]  
- [ ]  

### four

- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### five

- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### six

- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### seven 

- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### eight

- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 


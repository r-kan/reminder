# Reminder
better reminder, more customizable slideshow tool
==========================

Reminder, beyond an image slideshow tool, has the following unique features:  
1. can customize how the image is shown  
2. automatically search and download images  
3. can embed the image with customized phrases

P.S: for search function, `api_key` and `cx` of **google custom search** is required 

# System Requirement
python2.7

# Dependent Libraries
**Windows**  
1. make sure Tcl/Tk is installed in your python environment  
2. pip install `pillow-_version-num_.whl` (e.g., `Pillow-2.7.0-cp27-none-win_amd64.whl`)  
(find all pillow libraries at https://pypi.python.org/pypi/Pillow/2.7.0)  
3. pip install `requests`  

**Linux**  
1. apt-get install `python-tk`  
2. apt-get install `python-imaging-tk`  

**OSX**  
1. pip install `Pillow` 

# Sample usage
cd _reminder_target_directory_  
1. python main.py config.ini  
2. python main.py config_image.ini  
3. python main.py config_phrase.ini  

which demonstrate the following:  
1. image search/download/slideshow functionality  
2. show image by customized setting  
3. embed image with phrases  

# Hot keys
[Right]: next image  
[Left]: previous image  
[Esc]: switch fullscreen/window mode  
[i]: display image information  
[q]: exit application

# Contact
Please contact *rkan* by its_right@msn.com for any question/request/bug without hesitation.  

***
Watch screenshots and more information at http://r-kan.github.io/reminder/!

# eagletrt-matlab-dashbord
A local dashboard made with <b>MatLab</b> to easily plot telemetry data of <a href="https://github.com/eagletrt">@eagleTRT</a>
<h1>Project purpose</h1>
<p>This project was made for <a href="https://github.com/eagletrt">@eagleTRT</a>. The telemetry data are saved as a MongoDB. The purpose of this project is giving a fast and easy way to gaphically see, analize and compare data.</p> <p>For example data comparison allows to rapidly find discrepancies in power consumption related to the speed or to easily identify excessive temperature of the inverter or of the motors. It also manipulates data to provide real speed and slip coefficient. All this information can be used from mechanics team to find problems some mechanical problem or from dinamic team to improve some elements.</p> <p>The application should be used with desktop devices, mobile support was not needed.</p>
<br/>
<h1>Getting Started</h1>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes 
<h2>Prerequisites</h2>
You need a running installation of <a href="https://it.mathworks.com/products/matlab.html">MatLab R2019b</a> with installed the following addon:
<ul>
  <li><a href="https://it.mathworks.com/products/database.html?s_tid=FX_PR_info">Database Toolbox</a></li>
  <li><a href="https://it.mathworks.com/matlabcentral/fileexchange/64306-database-toolbox-interface-for-mongodb">Database Toolbox Interface for MongoDB</a></li>
</ul>
You need also a <a href="https://www.mongodb.com/cloud/atlas/lp/general/try?utm_source=google&utm_campaign=gs_emea_italy_search_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&gclid=EAIaIQobChMIlpKh5uWm6AIVCbrtCh08IAoQEAAYASAAEgL3HvD_BwE">MongoDB</a> installation to test the connection and import functions
<h2>Installing</h2>
Pull this repository into the matlab path or add the folder to it. Run Matlab and open Matlab App Designer from the APPS->Design App.
Now you can open the application files, all .mlapp files allow you to edit different windows of the application
<h1>Usage</h1>
<h2>Database connection</h2>
<<<<<<< HEAD
<img src="/docs_asset/connection_demo.gif">
=======
<br />
<p align="center">
  <img src="https://github.com/giorgio289/eagletrt-matlab-dashbord/blob/master/docs_assets/connection_demo.gif">
</p>
<br />
<p>From settings windows you can set parameters for the connection to your database(connection values are store in settings.mat file so they are used every time you run the connection until you change them). After properly set these parameters you can try to connect to the database: if connection fails you will recive an error else the lamp near to connection button will turn to green. After connection you can choose to close it with "chiudi" button</p>
>>>>>>> b37737dec93fc5ec8a787737f4d2adf6e95d101f
<h2>Import data from the Database</h2>
<br />
<p align="center">
  <img src="https://github.com/giorgio289/eagletrt-matlab-dashbord/blob/master/docs_assets/database_import_demo.gif">
</p>
<br />
<p>After connection enstablished you can import data from your Mongo database, you can choose source data from the dropdown menus: the first allows you to choose from the available collections and the second from the sessions stored in the selected collection. The structure of the documents in the database are stored in <a href="https://github.com/giorgio289/eagletrt-matlab-dashbord/blob/master/output.csv">output.csv</a> file which is generated form main.js which takes as input <a href="https://github.com/giorgio289/eagletrt-matlab-dashbord/blob/master/structure.json">structure.json</a> file (where is represented the structure of the documents as a tree).The tick under the menu allows you to choose if you want to save the imported session locally, that's good to reduce the time required to import the session in the future (the name of the file is the same as the name of the session and it is stored in the app folder)</p>
<h2>Import data from a local source</h2>
<br />
<p align="center">
  <img src="https://github.com/giorgio289/eagletrt-matlab-dashbord/blob/master/docs_assets/local_import_demo.gif">
</p>
<br />
If you have already saved a session you can quickly import it from local source selecting it from your storage (in the file is also stored the document structure so it is not required to edit the output.csv file if the document structure is changed)
<p></p>
<h2>Data plotting</h2>
<br />
<p align="center">
  <img src="https://github.com/giorgio289/eagletrt-matlab-dashbord/blob/master/docs_assets/diagram_plot_demo.gif">
</p>
<br />
<p>After data importation process completed a tree structure of the document is generated, selecting the leafs you can plot them to the diagram on the right. The diagram axis auto-adapts to the data which are selected. The switch on the top allows you to enable overlap function to easily compare data</p>
<br/>


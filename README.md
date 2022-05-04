# NFTExporter

## Requirements

Blender (tested with version 3.1.2)

Check the Blender installation with:
````
blender --version
````

## Setup

Clone the repo (default to ``~/`` directory, otherwise, need to change the ``save_path`` variable in ``config.py``):

````
git clone https://github.com/test-account-2021/nft-exporter.git
````

Put the Blender file on the root folder of the repo
````
nft-exporter/
    <filename>.blend
````

Open Blender through the console (so we can see error messages):
````
blender
````

## Generate the DNA

1. Disable export in ``config.py``.

````
enableExporter = False
````

2. In your .blend file open the ``Scripting Tab`` in the menu of Blender: 

<img width="1440" alt="Screen Shot 2021-10-24 at 9 51 25 PM" src="https://user-images.githubusercontent.com/82110564/138623488-9d0efc07-4004-4d3a-a7fe-25cb6050ac51.png">

3. Click the "Open" button in the Blender Text Editor:

<img width="1422" alt="Screen Shot 2021-10-29 at 11 31 38 PM" src="https://user-images.githubusercontent.com/82110564/139518856-7798ea86-0be0-4511-bc87-fa09ce2f6538.png">

4. With the Blender File View open, navigate to the NFTExporter folder, navigate to the ``src`` folder, then open main.py.

<img width="1062" alt="Screen Shot 2021-11-23 at 8 09 23 PM" src="https://user-images.githubusercontent.com/82110564/143153066-254e5e3e-cd06-4fdb-b645-180ed01fe89b.png">

5. To run ``main.py`` click the run button shown circled below:

<img width="605" alt="Screen Shot 2021-11-23 at 8 12 10 PM" src="https://user-images.githubusercontent.com/82110564/143153297-b90d9e16-69b7-4b44-b63b-20869f155f32.png">

You should now have the files ``NFTRecord.json`` and Batch#.json files located in the ``Batch_Json_files`` folder.

## Generating Images

1. Make sure to have followed ``Generate DNA`` section and have the files ``NFTRecord.json`` and ``Batch#.json``

2. Enable export in ``config.py``.

````
enableExporter = True
````

3. Run ``main.py`` in the Blender Scripting Tab. This will now generate the images to the ``NFT_Output/Batch#/Images``

<img width="605" alt="Screen Shot 2021-11-23 at 8 12 10 PM" src="https://user-images.githubusercontent.com/82110564/143153297-b90d9e16-69b7-4b44-b63b-20869f155f32.png">
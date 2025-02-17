# Purpose:
# This file determines the settings of your NFT collection. Please read the README.md file to understand how to run this
# program.

nftName = "Mintillionaire"  # The name of the NFT image produces by PNG-Generator

imageFileFormat = "PNG"  # Dictate the image extension when Blender renders the images
# Type the exact name provided below in the '' above:
# JPEG - Exports the .jpeg format
# PNG - Exports the .png format
# Visit https://docs.blender.org/api/current/bpy.types.Image.html#bpy.types.Image.file_format
# for a complete list of file formats supported by Blender. (Only use Image file extensions with imageFileFormat, 3D
# object, or animation file extensions will cause the program to fail)

animationFileFormat = (
    ""  # Dictate the animations extension when Blender renders and compiles the images
)
# Type the exact name provided below in the '' above:
# AVI_JPEG - Exports the .avi jpeg format
# AVI_RAW - Exports the .avi raw format
# FFMPEG - Encodes the video using ffmpeg. Set your encoding settings in the Output Properties in Blender. Default is
# medium-quality .mp4 video.
# Visit https://docs.blender.org/api/current/bpy.types.Image.html#bpy.types.Image.file_format
# for a complete list of file formats supported by Blender. (These are the Blender only supported animation formats)

modelFileFormat = "glb"  # The file format of the objects you would like to export
# Type the exact name provided below in the '' above:
# fbx - The .FBX file format
# glb - The .glb file format
# obj - The .obj file format *Exports both a .obj and a .mtl files for the same generated object
# x3d - The .x3d file format
# Visit https://docs.blender.org/api/current/bpy.ops.export_scene.html?highlight=export_scene#module-bpy.ops.export_scene
# for a complete list of object formats supported by Blender.

# The path to Blend_My_NFTs folder:
save_path_mac = "~/nft-exporter"
save_path_linux = "~/nft-exporter"
save_path_windows = r"C:\Users\pedro\Git\NFTExporter"
# Place the path in the '', e.g: save_path_mac = '/Users/Path/to/Blend_My_NFTs'
# Example mac: /Users/Path/to/Blend_My_NFTs
# Example linux: /Users/Path/to/Blend_My_NFTs
# Example windows: C:\Users\Path\to\Blend_My_NFTs

maxNFTs = 5  # The maximum number of NFTs you want to generate.
nftsPerBatch = 5  # Number of NFTs per batch
renderBatch = 1  # The batch number to render in Exporter.py

enableImages = True  # Renders and exports Images when main.py is run in Blender if enableExporter = True
enableAnimations = False  # Renders and exports Animations when main.py is run in Blender if enableExporter = True
enableModelsBlender = (
    True  # Generates 3D models when main.py is run in Blender if enableExporter = True
)
# ^^ Generates models with .blend file NOT external object library.

# Set to true to perform a lightbake before export. Only necessary when generating final output.
enableLightBake = False

# Enables Rarity_Sorter to weigh NFT DNA attributes and variants:
enableRarity = True
# generateColors must be turned off and enableMaxNFTs must be turned on.
# True = include weighted rarity percentages in NFTRecord.json calculations,
# False = Pure random selection of variants
# Note: The more attributes and variants you have, and by nature the more possible NFT combinations you have, the more
# accurate your percentages will be.

refactorBatchOrder = False  # When set to True, sorts, renames, and moves all NFTs files in all batches in NFT_Output
# folder to the Complete_Collection folder.
# After you generate all batches move them all to one computer and place them in the NFT_Output folder of Blend_My_NFTs.
# Run main.py with refactorBatchOrder set to True and all NFT files will be renamed and sorted into a folder called Complete_Collection.

# Meta Data Templates - Run after refactorBatchOrder
# Set the following to True to generate the format of the Meta Data template for your NFTs blockchain. (You can use multiple)
cardanoMetaData = False  # Cardano - Format Source: https://cips.cardano.org/cips/cip25/
solanaMetaData = False  # Solana - Format Source: https://docs.metaplex.com/nft-standard
erc721MetaData = False  # Ethereum ERC721 - Format Source: https://docs.opensea.io/docs/metadata-standards

turnNumsOff = True  # When set to True, turns off the extension numbers representing order and rarity from the names of
# variants in meta Data.

# NOTE: This is just the information Blend_My_NFTs can provide, you will have to add policy ID, URI information, etc
# yourself when you upload and mint your NFT collection.
# DISCLAIMER: These are only templates based on the common standards for the given blockchain, you will have to modify
# and fill them in with a script of your own when you mint your NFT collection. These metadata templates are only provided
# for your convenience and are as accurate to the standards above that I could make them.

metaDataDescription = (
    ""  # The description of your NFT that will be inserted into its meta data
)

# Set to True to generate images or 3D models depending on your settings below when main.py is run in Blender. Only works
# if you have already generated NFTRecord.json and all batches.
enableExporter = False

RENDER_RESOLUTION_PERCENTAGE = 200

# ADVANCED FEATURES:
### Select colour or material.###
# Object generation options:
enableGeneration = True  # When set to true this applies the sets of colors listed below to the objects in the collections named below

generationType = "material"  # You can either set 'color' or 'material' here. Type you set will correspond to following options.
# generationType = 'material' mode is experimental. Be sure that you back-up your file.
# You need to set materials as "fake user". Do not miss this step. Or your materials going to vanish after running this script.

# The collections below are RGBA Color values. You can put as many or as little color values in these lists as you would like.
# You can create any number of rgbaColorLists and assign them to any number of collections that you would like.
# Each set of rgbaColorList1 assigned to an object by collection name in the colorList will act like an attribute and create a unique variant of that item.

# PEDRO_BEGIN Adding colorway support
# pinkColorway = [(.456, .781, .826, 1)]
# blueColorway = [(.528, .445, .823, 1)]
pinkColorway = {
    "Colorway_1_0_Primary": (1.0, 0.820, 0.863, 1),
    "Colorway_1_0_Accent": (0.682, 0.775, 0.812, 1),
}

blueColorway = {
    "Colorway_2_0_Primary": (0.456, 0.781, 0.826, 1),
    "Colorway_2_0_Accent": (0.800, 0.730, 0.393, 1),
}

# PEDRO_END

# The following color list can be as long or as short as you want it to be.
# To use this all you need to do is place the name of the collection you want colored in the "" and the set of colors you want to apply to it after the :
# The collection named can only contain objects and not sub collections. Every object in the collection will be set to the colors you assigned above for each attribute

if generationType == "color":  # Do not change this line.
    # PEDRO_BEGIN Adding colorway support
    #    colorList = {"Colorway_1_0": primaryColorList}
    colorList = {"Colorway_1_0": pinkColorway, "Colorway_2_0": blueColorway}

# PEDRO_END

### These materials must be in your Current Files' Materials. Make sure that you've set your materials as "fake user". ###
# The collections below are Current Files' Materials. You can put as many or as little materials values in these lists as you would like.
# You can create any number of materialLists and assign them to any number of collections that you would like.
# Each set of materialLists assigned to an object by collection name in the materialList will act like an attribute and create a unique variant of that item.
materialList1 = [
    "Dollars_50",
    "Dollars_500",
    "Dollars_1000",
    "Euros_100",
    "Pounds_20",
    "Pounds_50",
    "Renminbi_20",
    "Renminbi_50",
    "Renminbi_100",
    "Ruble_500",
    "Ruble_1000",
    "Ruble_5000",
    "Sheckles_50",
    "Sheckles_100",
    "Sheckles_200",
    "Yen_1000",
    "Yen_2000",
    "Yen_5000",
]

materialRarityList = [
    0.25,
    0.25,
    0.25,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
]

initialDNAs = ['1-1-1-1', '1-1-2-1', '1-1-3-1', '1-1-4-1', '2-2-1-2', '2-2-2-2', '2-2-3-2', '2-2-4-2', '3-3-1-3', '3-3-2-3', '3-3-3-3', '3-3-4-3', '4-4-1-4', '4-4-2-4', '4-4-3-4', '4-4-4-4', '5-5-1-5', '5-5-2-5', '5-5-3-5', '5-5-4-5', '6-6-1-6', '6-6-2-6', '6-6-3-6', '6-6-4-6', '7-7-1-7', '7-7-2-7', '7-7-3-7', '7-7-4-7', '8-8-1-8', '8-8-2-8', '8-8-3-8', '8-8-4-8', '9-9-1-9', '9-9-2-9', '9-9-3-9', '9-9-4-9', '10-10-1-10', '10-10-2-10', '10-10-3-10', '10-10-4-10', '11-11-1-11', '11-11-2-11', '11-11-3-11', '11-11-4-11', '12-12-1-12', '12-12-2-12', '12-12-3-12', '12-12-4-12', '13-13-1-13', '13-13-2-13', '13-13-3-13', '13-13-4-13', '14-14-1-14', '14-14-2-14', '14-14-3-14', '14-14-4-14', '15-15-1-15', '15-15-2-15', '15-15-3-15', '15-15-4-15', '16-16-1-16', '16-16-2-16', '16-16-3-16', '16-16-4-16', '17-17-1-17', '17-17-2-17', '17-17-3-17', '17-17-4-17', '18-18-1-18', '18-18-2-18', '18-18-3-18', '18-18-4-18']



# The following material list can be as long or as short as you want it to be.
# To use this all you need to do is place the name of the collection you want materials assigned in the "" and the set of materials you want to apply to it after the :
# The collection named can only contain objects and not sub collections. Every object in the collection will be set to the materials you assigned above for each attribute
if generationType == "material":  # Do not change this line.
    colorList = {"A_1_0": materialList1, "B_1_0": materialList1, "C_1_0": materialList1}

enableResetViewport = True  # If True: turns all viewport and render cameras on after Image_Generator is finished operations

# 3D model imports and exports variables:
enable3DModels = False  # Set to True if using external models as attributes instead of Blender objects
# ^Does not work with colour options and rarity, both must be turned off in order to use this.

# Tests and Previews:

# Preview and render test settings:
# Set to True to run Preview test, set to False to stop test. Run main.py in Blender to initiate the test. Results will
# be displayed in the Blender terminal or console. enableExporter must be False, and enableImages and/or enableModelsBlender
# to run a preview.
runPreview = False
maxNFTsTest = 5  # Increase to get a more accurate reading of the render time. The number of images generated in the render test.

# Turn this on when you run main.py to generate NFTRecord.json and appropriate batches to confirm there are no duplicate
# NFT DNA. Note - This file is provided for transparency, it is impossible for duplicates to be made with the current code in
# DNA_Generator.py.
checkDups = False

# Turn this on when running main.py to generate NFTRecord.json and Batch#.json files to record the rarity percentage of each variant.
# Note - This file is provided for transparency. The accuracy of the rarity values you set in your .blend file as outlined
# in the README.md file are dependent on the maxNFTs, and the maximum number of combinations of your NFT collection.
checkRarity = True

# Utilities - DO NOT TOUCH:
import platform
import os

mac = "Darwin"
linux = "Linux"
windows = "Windows"
slash = ""
save_path = None

# Save_path utilities and os compatibility
if platform.system() == mac:
    save_path = os.path.expanduser(save_path_mac)
    slash = "/"
elif platform.system() == linux:
    save_path = os.path.expanduser(save_path_linux)
    slash = "/"
elif platform.system() == windows:
    save_path = save_path_windows
    slash = "\\"

# Paths to folders
batch_json_save_path = (
    save_path + slash + "Batch_Json_files"
)  # The output path for batches generated by Batch_Sorter.py
nft_save_path = (
    save_path + slash + "NFT_Output"
)  # The output path for images generated by Exporter.py
modelAssetPath = save_path + slash + "3D_Model_Input"  # The input path for 3D models
model_save_path = (
    save_path + slash + "3D_Model_Output"
)  # The output path for 3D models generated by Model_Generator.py
model_Script_Ignore_Path = (
    modelAssetPath + slash + "Script_Ignore_Folder"
)  # The path to the Script_Ignore_Folder for 3D models

# error handling #
if modelFileFormat not in ["fbx", "glb", "obj", "x3d"] and enable3DModels:
    raise ValueError(
        "Output format in `objectFormatExport` can only be 'fbx', 'glb', 'obj', 'x3d'."
    )

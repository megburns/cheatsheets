from http.server import executable 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep 
from tabulate import tabulate 



options = """
options:
1. Modem Info
2. Troubleshooting
3. Common Terminal Commands
"""
print(options)
val = int(input('Enter a number option: '))


DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"

if val == 1:
    print("Modem Info")

    options1 = """
    1. Canada SIM
    2. Gen5
    3. Wide (Old Hardware)
    4. Dolphin
    5. ccNc
    6. Value 2
    """

    print(options1)
    opt = int(input('Enter a number option: '))

    if opt == 1:
        print("Canada SIM")
       

        data1 = [[ "Bell", "Tele","HACC	", "MOBISCANADA000008", "?",355508027854531, "Deactivated", " ", "Gen4?"],
            [ "Bell", "SQA", "KCI", "MOBISSK3027836710", 89302690201001689390,355508027836710,  6479021689, "Not CCS", "Modem Not Found"],
            [ "Bell", "Tele", "KCI", "MOBISSK3027836736", 89302690201001684052, 355508027836736, 7145144121, "Active", "Modem Not Found" ],
            ["Bell", "Tele", "KCI", "MOBISSK3027836694",89302690201001689291, 355508027836694, 6479021679, "Active", "Active", "Modem Not Found"],
            ["Bell", "TD", "KCI", "MOBISTEST70961777",89302690201001498149,352756070961777, 6479020604, "Not CCS", "Gen4?"  ],
            ["Bell", "Tele", "KCI", "MOBISTEST82084793 ", 89302690201001342669, 355508027820847, "Deactivated", " ", "Modem Not Found"]]

        header1 = ["Carrier", "Team", "ENV", "VIN", "ICCID", "IMEI", "MDN", "Status(Tri)", "Platform"]
        
        print(tabulate(data1, headers=header1, tablefmt="grid"))
    elif opt == 2:
        print("Gen5")

        data2 = [["Verizon", "Tele", "KMA", "MOBISTSTSTG160701", 89148000002104532376, 355182060201925, 7145144121, "Active"],
                ["Verizon", "TD", "HMA", "5NPE34AF4FT890678",89148000002171924712, 359554061896018, 6472096851, "Not CCS"],
                ["Verizon", "Tele", "KMA", "TESTVINST10191701", 89148000002361920116, 358885060082015, 6573054876, "Active"],
                ["Bell", "Tele", "HACC", "HATAPDG510011VINP", 89302690201002849902, 352756072175020, "Deactivated", " "],
                ["Verizon", "?", "HMA", "5NPE24AF2GT082415", 89148000002051549514, 358885060016708, "Deactivated", " "]]

        header2 = ["Carrier","Team", "ENV", "VIN", "ICCID", "IMEI", "MDN", "Status(Tri)"]

        print(tabulate(data2, headers=header2, tablefmt="grid"))

    elif opt == 3:
        print("Wide(Old Hardware)")

        data3 = [["Verizon", "Tele", "HMA", "5NPE34AF1JT041018", 89148000003427492769, 357186082203122, 7146252676, "Deactivated"],
                ["Verizon", "Tele", "KMA", "TESTVINST05221803",89148000003427492777, 357186082203148,6573109188, "Active"],
                ["Verizon", "Tele", "KMA", "TESTVINST05221801", 89148000003427498204, 355508027854994,6573109185, "Active"],
                ["Verizon", "Tele", "KMA", "TESTVINST05221802",89148000003427498154, 355508027855140,6573109186, "Active"],
                ["Verizon", "HD", "KMA", "TESTVINST04191801", 89148000003427498287, 355508027855124, "NA", "Deactivated"],
                ["Verizon", "TD", "HMA", "5NPE34AF9JT043518", 89148000003427474825, 352756072795637,6572836880, "Not CCS" ],
                ["Bell", "?", "KCI", "TEST275607318581", "?",352756073185812, 14318057027, "Deactivated" ],
                ["Verizon", "HD", "KMA", "TESTVINST05291802",89148000003298149779, 355508027849366, "NA", "Deactivated" ],
                ["?", "HD", "-", "-", 89148000003298149894, 355508027849770, 6572602531, "Deactivated" ],
                ["?", "Tele", "-", "-",89148000003427497859, 355508027854853, "NA", "Deactivated" ]]
       
        header3 = ["Carrier","Team", "ENV", "VIN", "ICCID", "IMEI", "MDN", "Status(Tri)"]

        print(tabulate(data3, headers=header3, tablefmt="grid"))

    elif opt == 4:

        print("Dolphin")

        data4 = [["Carrier", "Team", "ENV", "VIN", "ICCID", "IMEI", "MDN"]]

        print(tabulate(data4, tablefmt="grid"))
    
    elif opt ==5:

        print("ccNC")

        text1 = """
        cd /ccos/data/services/diagnosisservice/keyvalue/
        sqlite3 shared.db
        update hkeyvalue set value="" where key="key_dummy_vin";
        update hkeyvalue set value="" where key="key_main_vin";
        """

        print(text1)


        data5 = [["Verizon", "SQA", "HMA", "KM8K53A3XNT315930",89148000006902284601,351478317805623,5268489662, "Not CCS"  ],
                ["Verizon", "Tele", "KMA", "CCNCSTGDEV0000001",89148000006902284940, 351478317806191,5025422859, "Active"  ],
                ["Verizon", "SQA", "KMA", "CCNCSTGDEV0000003", 89148000006902285046, 351478317805342,5026825929, "Not CCS" ],
                ["Verizon", "Tele", "HMA", "KMUKBDTC7MT316898",89148000006902284544,351478317805664, 5268489653, "Active"  ],
                ["Verizon", "Tele", "HMA", "KMUKBDTC9MT316899", 89148000006902284460, 351478317805649, 5268489662, "Active"]]

        header5 = ["Carrier","Team", "ENV", "VIN", "ICCID", "IMEI", "MDN", "Status(Tri)"]

        print(tabulate(data5, headers=header5, tablefmt="grid"))

    else:

        print("Value 2")

        text2 = """
        insert into Vehicle (id,name,value) VALUES(1,"VehicleVin","");
        update Common set value=1 where name="AntennaCheckEnable";
        """

        print(text2)

        data6 = [["Verizon", "Tele", "KMA", "TESTVINSWDEV10001",89148000004920672923,352756074001877, 6574314064, "Deactivated"  ],
                ["Verizon", "Tele", "KMA", "TESTVINSWDEV10002", 89148000004920671818,352756074002917,5023952150, "Active"  ],
                ["Bell", "Tele", "KCI", "TEST2756073981053",89302690201007052718,352756073981053,16476637225,"Deactivated"   ],
                ["Vivo", "MTCA", "BRZ", "BRTESTCAR00000019",89551080257000000542,357186082269222, "+5511942576247", "Active"  ],
                ["Verizon", "TD", "HMA", "KMHC05LCXKT310413", " ", 352756075271685, 6573964710, "Not CCS"]]
                
        header6 = ["Carrier","Team", "ENV", "VIN", "ICCID", "IMEI", "MDN", "Status(Tri)"]

        print(tabulate(data6, headers=header6, tablefmt="grid"))
        
elif val == 2:
    print("Troubleshooting")

    options2= """
    1. Not getting provision from modemless UVO
    2. Debuggin for the H/U
    3. How to activate provision states
    4. Submitting a PR to Bitbucket
    5. Touchscreen compatibility issue
    6. Target build not appearing on lunch list
    7. Failed to build a target (Article with possibility of extension)
    8. Target build not appearing in lunch.
    9. How to activate Valet Mode manually.
    10. How to trigger an ACN/911 call.
    11. How to enable adb from your H/U
    12. Most meaningful apps of telematics.
    13. Path where digital products are (target builds)
    14. Project cannot find activity or other component even though is still added into manifest.xl
    15. Location for relevant French and Spanish language folders
    16. How to trigger an Info Big datafile
    17. Project fails to build due to some random fatal error in Java
    18. Android studio doesn't show up all projects
    19. How to trigger an ACN call manually
    20. How to trigger a POI
    21. Apps to rename .mk file in order to shrink the project enough to build
    22. How to trigger engine on
    23. CAN filters
    24. Path to VCRM settings in sqlite 
    """

    opt1 = int(input('Enter a number option: '))

    if opt1 == 1:
        print("Not gettering provision from modemless UVO")

        out1 = """
        1-Go to frameworks/services

        2-Run git status

        Check if SystemService.java has changes that are making non-modem UVO accessible since it could potentially create conflicts with All Menu activity.
        """

        print(out1)
    elif opt1 == 2:
        print("Debuggin for the H/U")

        out2 ="""
        To make debugging on the H/U it is necessary to pair it with Android Studio through adb

        To check whether the .apk and .odex files were pushed successfully into the H/U use md5sum to check if the code id are the same. To do this, identify the code ID from the APK file in terminal by going to the location where the file is and type:

        md5sum <apk file name>

        Write down the code it shows.

        To check the code ID on the H/U, type on terminal (it doesn't matter from where as long as adb is enabled):

        busybox md5sum <apk file name>

        Note: busybox doesn't actually work to check the md5sum on a H/U. This needs further verification.

        Write down the code id and compare.
        """

        print(out2)
    elif opt1 == 3:
        print("How to activate provision states ")

        out3="""
        1-Use adb to open the H/U shell: adb shell

        2-Open the vehicle setting database: sqlite3 /data/data/com.hkmc.telematics.common.db/databases/VehicleSetting.db

        3-Type: update prov_info set Status={int value};
        """

        print(out3)

    elif opt1 == 4:
        print("Submitting a PR to Bitbucket")

        out4= """
        Note: This probably should have its own page.

        Once changes have been committed to the branch, proceed on doing the following.

        1-Push your changes to master branch and have them reviewed.

        2-If accepted, branch will be merged.

        3-After merging (is not necessarily to have them merge before doing this) go to where the commit is.

        4-Look at the top right of the screen and click Cherry-Pick.

        5-A screen wil pop-up and will ask where to make the commit

        6-Select which target branch are you commit this changes.

        Note: To know which target branch you are looking for, go to the confluence page,


        Look up for the latest branch. Usually, the North American region is the one we work at, however, other regions might also need to be worked on if your changes are global (affect all regions).

        After you have selected the right brand, click Cherry.

        7-The screen will take you to a Create pull request screen, where you have to type a description of the ticket you just solved. Is important to find the right reviewer on Korea to check your changes.This can be verified on the confluence pager visited before.
        """

        print(out4)

    elif opt1 == 5:
        print("Touchscreen compatibility issue")

        out5= """
        1. Open the .mk file of the model you are working on. (i.e ql21_us.mk)
        2. Search for the line "PRODUCT_INCLUDE_LCD_8_INCELL:=true"
        3. If the line is present, delete it, save, and exit. If the line is not present, add it, save, and exit.
        4. Build again. Make sure to run "make clean" before that.
      if this doesn't work, also try the following. In the same .mk, add the line:

        1. "USE_KMC_NEW_GUI:=true"
        2. Build again and make sure to run "make clean" before that
        """
        print(out5)

    elif opt1 == 6:
        print("Target build not appearing on lunch list")

        out6 = """
        In case target build does not appear on lunch list, this means that the build has not been added yet on vendorsetup.sh file. In order to fix this, you should go to the following location:

        ...mobis/daudio/product/vendorsetup.sh

        1- Edit vendorsetup.sh

        2- Type: add_lunch_combo <target build>

        3- Save changes and exit.

        4- Run lunch again on the docker container

        Target build should appear there.
        """

        print(out6)


    elif opt1 == 7:
        print("Failed to build a target (Article with possibility of extension)")

        out7= """
        Sometimes, build process from Gen 5 project will fail after pulling off from master branch. This could be due to several apps and each issue may be addressed by trying some of the following fixes:

        1.- Failed to allocate x amount of blocks

        This build error is apparently caused by exceeding the size of the system partition. A possible solution for this is to exclude unused apps (Note: why not delete them already then?) from the target build. In order to do this, you must go to where the Android.mk file of an especific app (i.e HKMC_VLS ) is located and proceed to rename it to Android.mk_.

        If this change does not make the build to work correctly, proceed to exclude more apps from the build process. Some of them could be:

        .-HKMC_USBMusic

        .-HKMC_NatureSound

        .-HKMC_USBVideo

        .-HKMC_USBImage

        .-HKMC_InteractiveGuide

        .-HKMC_NaviInteractiveGuide


        Most of these packages will be located in the path:

        (source root)/packages/apps/HKMC_

        Except for _NatureSound which is located in:

        (source root)/vendor/mobis/packages/apps/HKMC_

        2.- Another solution could be just relocation more memory into the docker container.

        Our modern desktop pc's are heavily equiped with an AMD Ryzen 9 3950x 16-Core Processor with 128G RAM so you should feel confident on allocating more than 32G on the container.

        To do this, open a terminal window and type:

        docker run --rm -m='x'g -v /(path where your source code is located)/Gen5/:/data -it daudio

        Where 'x' is the amount of memory you want to allocate. As previously mentioned, 32g is the usual ammount but allocating this to 64g or 128g may solve the building issue.
        """

        print(out7)


    elif opt1 == 8:
        print("Target build not appearing in lunch.")

        out8= """
        If the target build does not appear on the lunch list, first verify that the target .mk file is located in the following path:

        (Source Code)/device/mobis/daudio/products

        After confirming the existence of the .mk file, open the file vendorsetup.sh and type the following at the end of the file:

        add_lunch_combo <name of target>

        Next time you should type on the docker container:

        source build/envsetup.sh

        Then the target build you just added should appear on the lunch list.
        """

        print(out8)


    elif opt1 == 9:
        print("How to activate Valet Mode manually.")
     
        out9 = """
        You need to have adb active in your H/U.

        Type:

        1-adb shell

        2-am start -n com.hkmc.telematics.apps.Vrm.main/com.hkmc.telematics.apps.Vrm.valetMode.ui.ValetModePWSettingActivityNew
        """

        print(out9)


    elif opt1 == 10:
        print("How to trigger an ACN/911 call.")

        out10 = """
        You need to have adb active in your H/U.

        1-adb shell

        2-am broadcast -a com.hkmc.telematics.service.ACN_OCCURS
        """
        print(out10)

    elif opt1 == 11:
        print("How to enable adb from your H/U")

        out11 = """
        Before attempting this, make sure you have minicom installed on your desktop pc.

        1- On terminal, type: sudo minicom -s

        2-A window will pop up on terminal title "configuration". Go to serial port setup.

        3-Change Serial Device setting by typing: shift + a

        4-Change Serial Device setting from /dev/modem to /dev/ttyUSB0. Hit enter after you are done.

        Note:ttyUSB0 is usually the usb port we have for our desktop machines, which have similar hardware setup. Port number may vary for machines. You may need to figure out which port you are using.

        5- Change Hardware Flow Control from yes to no by typing: "shift + f". Then hit enter to toogle the value.

        6-Hit Esc and pick Exit (do not pick Exit from Minicom).

        7-On the shell, type: su

        8-Type: setprop persist.sys.dipo.state debug

        9-You are done enabling adb from the H/U.

        Your H/U should have its adb enabled on terminal.
        """

        print(out11)

    elif opt1 == 12:
        print("Most meaningful apps of telematics.")

        out12 = """
        -HKMC_TAppService -> Handles web request/responses

        -HKMC_TAppVRM -> Handles UI for most of telematics

        -HKMC_TAppSafety -> Additional UI handling that is not present on TAppVRM (i.e POI features)
        """
        print(out12)

    elif opt1 == 13:
        print("Path where digital products are (target builds)")

        out13 = """
        /xref/daudio/device/mobis/daudio/product/
        """
        print(out13)

    elif opt1 == 14:
        print("Project cannot find activity or other component even though is still added into manifest.xl")

        out14 = """
        This may occasionally happens once in a while when making changes on a certain module of the apps when applying new software separately.

        One possible solution for this is to do a full buildall while varying the number of working threads assigned to it and restart the H/U.
        """
        print(out14)


    elif opt1 == 15:
        print("Location for relevant French and Spanish language folders")

        out15 = """
        -values-fr-rCA -values-es-rUS
        """
        print(out15)

    elif opt1 == 16:
        print("How to trigger an Info Big datafile")

        out16="""
        1- Have ACC on in your H/U 2- Use CAN simulator to trigger an ACN 3- Have IGN and ACC off 4- Go to TOS and search using the VIN currently being used by the H/U 5-Find the IBD-V service 6-Copy what appears inside of "infoBigDataInfo": (will be a big encoded paragraph) and decode it using:

        httpsl://www.base64decode.org/

        This will decode it to the json file info and can be format it through a json beautifier.

        In addition to the previous steps, it should be possible to extract directly the json file from the H/U with the following steps:

        While adb is active.

        1- adb shell am broadcast -a com.hkmc.system.app.engineer.intent.action.VCRM_MODE --ez vcrm_mode ""true"" command

        Note: Not sure if command is actually part of the statement.

        2- After operation, extract and check the infoBigData_settingInfo.json and infoBIgData_usafeInfo.json files in the /storage/log/vcrm_log folder

        Note: Files will only be generated with ACC off
        """
        print(out16)

    elif opt1 == 17:
        print("Project fails to build due to some random fatal error in Java")

        out17 = """
        Sometimes, an error will prompt while building complaining that Java is having issues dealing with the working threads.

        Usually, buildall -j{x} takes 32 int as {x} parameter. Switching this to a lower int might solve this issue (i.e 30, 16).
        """
        print(out17)

    elif opt1 == 18:
        print("Android studio doesn't show up all projects")

        out18="""
        This may happens sometimes while working on Android studio. The easiest and straight forward way to fix this is by deleting the .idea file on the repository you are working on (i.e HKMC_TAppVRM) and then restart Android studio.
         """

        print(out18)

    elif opt1 == 19:
        print("How to trigger an ACN call manually")

        out19 = """
        1-Get minicom and adb ready. 2-Type: adb shell 3-Type: am broadcast -a com.hkmc.telematics.service.ACN_OCCURS
        """
        print(out19)

    elif opt1 == 20:
        print("How to trigger a POI")

        out20="""
        1-Get minicom and adb ready.ls 2-Type: adb shell 3-Type: am broadcast -a com.hkmc.intent.action.POI_SHORTCUT
        """

        print(out20)
    elif opt1 == 21:
        print("Apps to rename .mk file in order to shrink the project enough to build")

        out21="""
        (source root)/packages/apps/HKMC_InteractiveGuide (source root)/packages/apps/HKMC_NaviInteractiveGuide (source root)/packages/apps/HKMC_USBVideo (source root)/packages/apps/HKMC_USBMusic (source root)/packages/apps/HKMC_USBImage (source root)/vendor/mobis/packages/apps/HKMC_NatureSound

        [Add more apps that might help lower the project size without compromising its building]
        """
        print(out21)

    elif opt1 == 22:
        print("How to trigger engine on")

        out22= """
        Send the following intent through adb shell:

        am broadcast -a com.hkmc.telematics.service.AlertService.action_noti_geofence_service
        """

        print(out22)

    elif opt1 == 23:
        print("CAN filters")

        out23="""
        System.out|brightness|engine|speed|ACC|TAS_HS|BlackScreenService|CAN_MANAGER|SystemService|VehicleInfoManager|speed|Micom|ClusterService|Light|fuel|BCMService|crash
        """
        print(out23)

    else:
        print("Path to VCRM settings in sqlite")

        out24="""
        /data/data/com.hkmc.telematics.common.db/databases/VCRMSetting.db
        """

        print(out24)


else:
    print("Common Terminal Commands")

    commands = """
    List of common terminal commands:

    change directory: cd
    listing directory: ls
    open files: open
    copy a file to another directory: cp
    move a file: mv
    create a text file: touch
    create a directory: mkdir
    remove an empty directory: rmdir
    remove nested directories: rm -R
    execute commands with superuser privileges: sudo
    list actively running computer processes: top
    quit sub-screen and return to terminal: q
    clear the terminal screen of all previous commands: clear
    copy contents of folder to a new folder: ditto
    get one-line description for a command: whatis 
    show manual page for a command: man
    the "exit" command: exit
    calls a batch file from another one: call
    clear screen: cls
    list directory content: dir
    terminate a process or an application: taskkill
    display applications and related tasks: tasklist
    """
    print(commands)




  
 













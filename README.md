![build](https://img.shields.io/badge/build-passing-brightgreen) ![license](https://img.shields.io/badge/license-MIT-brightgreen) ![python](https://img.shields.io/badge/python-3.9%2B-blue) ![platform](https://img.shields.io/badge/platform-linux--64%20%7C%20win--64-lightgrey)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MinionAttack_WeddingPhotoDownloader&metric=alert_status)](https://sonarcloud.io/dashboard?id=MinionAttack_WeddingPhotoDownloader)

# Weeding Photo Downloader

Table of contents.

1. [Author disclaimer](#author-disclaimer)
2. [Introduction](#introduction)
3. [Requisites](#requisites)
4. [Project structure](#project-structure)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [How to use](#how-to-use)
8. [Licensing agreement](#licensing-agreement)

## Author disclaimer

This project has been carried out solely and exclusively for self-learning reasons and to show it as a career portfolio.

When scrapping websites, make sure you do so in a responsible manner so as not to cause any harm to the website or the
users who use it.

I am not, nor will I be responsible for any misuse of the code of this project by third parties.

## Introduction

After more than 15 years of using Firefox with ad blockers there comes a point where you internalise how web pages
should look as you are used to seeing them that way and not without ad blockers, or worse, forget that you have an ad
blocker enabled.

So, after attending the wedding of some friends, I received links to the websites where the photography company had
uploaded all the material from the party. In this case, the problem was assuming that the website was what it looked
like in my browser and forgetting that I had the ad blocker enabled.

When I first accessed the website it looked like this:

![NoSocialBanner](docs/img/NoSocialBanner.png)

At first glance it doesn't look unusual, it's not the best web design, but it works. So after seeing that and given the
huge amount of items to download, there was no way I was going to do it by hand.

When I got around to programming this project and after getting Selenium set up, I launched the script for the first
time and it started a new instance of Firefox with no add-ons, so when it loaded the same website it looked like this:

![SocialBanner](docs/img/SocialBanner.png)

At this point I had almost half of the code done, plus all the time invested to make it work, so I decided to finish it
as a personal challenge.

## Requisites

In order to use the script it is necessary to have a compatible environment:

- **Operative system**: A Linux or Windows based system where the script will run.
- **Python version**: The script has been developed with version **3.10**. It uses some features that are only available
  from version **3.9 onwards**.

## Project structure

In this section you can have a quick view of the project structure.

```
.
├── docs
│   └── img
│       ├── NoSocialBanner.png
│       └── SocialBanner.png
├── LICENSE
├── logs (*)
│   ├── critical.log
│   ├── debug.log
│   ├── error.log
│   ├── geckodriver.log
│   ├── info.log
│   └── warning.log
├── modules
│   ├── DownloadManager.py
│   ├── NetworkManager.py
│   └── StorageManager.py
├── README.md
├── requirements.txt
├── resources
│   ├── configuration.py
│   └── log.yaml
├── src
│   ├── logger.py
│   └── main.py
└── utils
    ├── FirefoxConfigurator.py
    ├── GalleryItem.py
    ├── HumanBytes.py
    └── Messages.py
```

Directories marked with a (*) will be created by the script as needed.

## Installation

This section expects the requirements stated in the previous section to be met and this is how this section has been
written.

- **GeckoDriver**: The driver that Selenium uses to interact with Firefox.
  - Download the file from the GitHub repository ([Link][1])
  - Place it in `/usr/bin` or `/usr/local/bin` directory (you may need administrator permission).
- **Program dependencies**: The script has some dependencies that must be installed in order to work. Those dependencies
  can be installed with the _requirements.txt_ file:
  - `pip install -r requirements.txt`
- It is highly recommended to use a **virtual environment** (*venv*), so the script dependencies installation will not
  conflict with the packages installed on the system.

If you want to run the script in a *venv*, open a terminal in the project's root folder and run:

```
source path_to_your_virtual_environment/bin/activate
pip install -r requirements.txt
```

If you do not want to run the script in a *venv*, open a terminal in the project's root folder and run:

```
pip install -r requirements.txt
```

**Note**: If you have both **Python 2** and **Python 3** installed on your system, use **pip3** instead of **pip**.

[1]: https://github.com/mozilla/geckodriver/releases

## Configuration

There are some parameters that need to be set by the user, so the script can work. Those parameters are in the
*/resources/configuration.py* file.

- **GECKODRIVER_PATH**: Due to recent changes, Selenium may fail to create the Firefox instance if the browser comes
  pre-installed via SNAP instead of installing it with apt-get. To prevent this error from occurring, the correct path
  must be given to the driver.
  - Open a terminal and run:
  ```
  $ whereis geckodriver
  geckodriver: /usr/bin/geckodriver /snap/bin/geckodriver
  ```
  - If there is an option with SNAP you have to specify that one, otherwise specify the one that appears.

- Currently, the script is made to work on galleries hosted at [fotoshare cloud][2]. If in the future you need to update
  the values or want to adapt the script to another hosting site, please modify the variables after the comment:
  ```
  Modify these variables below in case the script stops working or you want to use another website
  ```
  in the `resources/configuration.py` file.

[2]: https://fotoshare.co/

## How to use

- Remember to activate the `venv` if you are using it.
- Add the root folder of the script to Python's path variable:
  ```
  $ export PYTHONPATH=$PYTHONPATH:/full/path/script/root/folder/
  ```
- Go to the `src` folder of the project and grant execute permissions to `main.py` file:
  ```
  $ chmod +x main.py
  ```
- Start the script:
  ```
  $ python3 main.py
  ```

This will show the usage:

```
usage: main.py [-h] {download} ...

Get the wedding photos and videos from the web gallery

options:
  -h, --help  show this help message and exit

Commands:
  {download}
    download  Download the web gallery
```

If you need instructions on how to use the `download` command, type:

  ```
  $ python3 main.py download -h
  ```

This will show the usage:

```
usage: main.py download [-h] --gallery GALLERY [GALLERY ...] --name NAME

options:
  -h, --help            show this help message and exit
  --gallery GALLERY [GALLERY ...]
                        A list of gallery identifiers, separated by a space
  --name NAME           Name of the folder where the galleries will be downloaded
```

### Example of use

The following is an example of use:

```
download --gallery gallery_id_1 gallery_id_2 --name MyWeddingAlbum
```

**Note**: If the folder name contains spaces, it must be enclosed in double quotes.

```
download --gallery gallery_id_1 gallery_id_2 --name "My Wedding Album"
```

## Licensing agreement

Copyright © 2023 MinionAttack

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

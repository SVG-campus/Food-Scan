# Python Keras Fruit and Vegetable (+Food) Scanning Tool

Sample Scanning ML tool built on [visual studio code](https://code.visualstudio.com/).

Language| Framework | Runtime | Platform | Author |
| --------| -------- | -------- |--------|--------|
Python | Tensorflow | Keras | On-site| OpenAI |

### Python
- #### Python installation on Windows

  Just go on [official Node.js website](https://nodejs.org/) and download the installer.
Also, be sure to have `git` available in your PATH, `npm` might need it (You can find git [here](https://git-scm.com/)).


### Pip
- #### Pip installation on Windows

  Just go on [official Node.js website](https://nodejs.org/) and download the installer.
Also, be sure to have `git` available in your PATH, `npm` might need it (You can find git [here](https://git-scm.com/)).


## Installation

For development, you will need Python 

      $ pip install -r requirements.txt

- #### Running Pythong Scripts
  You can find more information about the installation on the [official Node.js website](https://nodejs.org/) and the [official NPM website](https://npmjs.org/).

If the installation was successful, you should be able to run the following command.

    $ python download_dataset.py
      "Dataset downloaded to:" [path]
      
If you need to update `npm`, you can make it using `npm`! Cool right? After running the following command, just open again the command line and be happy.

    $ python train_model.py

for test_model.py change predict_ripeness("path_to_test_image.jpg")  # Replace with actual test image path

    $ python test_model.py

## Deploying on IBM

Any change to this repository will result in triggering a workflow to build and deploy this app on azure as an app service. Learn more about [Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/) and [Github Actions](https://docs.github.com/en/actions).

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


## License:

See [LICENSE](LICENSE).

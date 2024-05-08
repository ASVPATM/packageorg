# packageorg
Organizes a copy and paste list from (either pip or brew), and organizes them into a new file where each package has its own individual line

Meant to be really simple so you can store your packages in a way so that you can quickly install reinstall them if needed

- However you will need to keep updating/creating new txt files as you add more packages, which might not be that efficient 
- Also looking to update script so that you can be able to provide an old list of organized packages and then the current list of your packages so that it can look at both lists and then remove the duplicates and add new packages to a new list txt

Homebrew Bundler --> https://github.com/Homebrew/homebrew-bundle.git

**Pip Packages Example**

<img width="500" alt="Screenshot 2024-05-07 at 19 49 08" src="https://github.com/ASVPATM/packageorg/assets/159084542/119dbc04-cd29-4323-bf27-5f70b12a7f02">

- Pasted into file && Output of Program                                     

<img width="500" alt="Screenshot 2024-05-07 at 19 55 51" src="https://github.com/ASVPATM/packageorg/assets/159084542/7681fb29-234e-4cd4-a55e-9892374da19b">
<img width="500" alt="Screenshot 2024-05-07 at 20 00 56" src="https://github.com/ASVPATM/packageorg/assets/159084542/39041237-6235-47ac-98c4-10c1fc76fc21">

**Brew Formulae Example**

<img width="500" alt="Screenshot 2024-05-07 at 19 53 02" src="https://github.com/ASVPATM/packageorg/assets/159084542/13f7af7e-5acc-44c3-ad3a-6e1903588a7f">

- Pasted into file && Output of Program

<img width="500" alt="Screenshot 2024-05-07 at 20 18 17" src="https://github.com/ASVPATM/packageorg/assets/159084542/b500d14b-50d3-4256-b067-a1be7cd42bd1">
<img width="500" alt="Screenshot 2024-05-07 at 20 17 16" src="https://github.com/ASVPATM/packageorg/assets/159084542/31c0bdd8-a87a-48ce-914e-e08d0c539c81">

- script

$$$ python3 org.py

$$$ Enter the path to the input text file: xxxxxxxx

$$$ (prints output)

$$$ Do you want to write the processed content to a new file? (yes/no): yes

$$$ Enter the path to the output text file: xxxxxxxx

$$$ Processed content written to 'xxxxxxxx'

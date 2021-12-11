### Install Anaconda from command line style (Hyper zsh)

Step 1: Curl the shell script for Anaconda.

    curl https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.sh

Step 2: Provide permission for the script before running.

    chmod 755 Anaconda3-2020.11-MacOSX-x86_64.sh 

Step 3: Run the shell script for installation.

    ./Anaconda3-2020.11-MacOSX-x86_64.sh 

After accepting “End User License Agreement - Anaconda Individual Edition” either accept the prompted default location or provide a new location for installation. 


Step 4: Activate

    source /Users/<username>/anaconda3/bin/activate

Note: Replace <username> with your user name.

Step 5: Run conda initialization
    
    conda init
    
Note: conda init is available in conda versions 4.6.12 and later.
    
Step 6: Close and open a new shell after conda initialization

Step 7: Verify installation

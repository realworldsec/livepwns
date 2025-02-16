#!/bin/bash

# Update package list and install massdns
echo "Installing massdns..."
sudo apt install -y massdns

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Clone Sublist3r if it doesn't already exist
if [ ! -d "Sublist3r" ]; then
    git clone https://github.com/aboul3la/Sublist3r.git
    echo "Sublist3r has been cloned."
else
    echo "Sublist3r already exists. Skipping cloning."
fi

# Clone dirsearch if it doesn't already exist
if [ ! -d "dirsearch" ]; then
    git clone https://github.com/maurosoria/dirsearch.git --depth 1
    echo "dirsearch has been cloned."

    # Install additional dependencies for dirsearch
    echo "Installing additional dependencies for dirsearch..."
    pip install --break-system-packages --user PySocks>=1.7.1 Jinja2>=3.0.0 defusedxml>=0.7.0 pyopenssl>=21.0.0 requests>=2.27.0 \
                requests_ntlm>=1.3.0 colorama>=0.4.4 ntlm_auth>=1.5.0 beautifulsoup4>=4.8.0 \
                mysql-connector-python>=8.0.20 psycopg[binary]>=3.0 defusedcsv>=2.0.0 \
                requests-toolbelt>=1.0.0 setuptools>=66.0.0 httpx>=0.27.2 httpx-ntlm>=1.4.0
else
    echo "dirsearch already exists. Skipping cloning."
fi

# Add Sublist3r and dirsearch to the PATH (environment variable)
export PATH=$PATH:$(pwd)/Sublist3r:$(pwd)/dirsearch

# Make the change permanent by adding it to the shell profile
echo 'export PATH=$PATH:'$(pwd)/Sublist3r:$(pwd)/dirsearch >> ~/.bashrc

# Automatically apply the changes to the current shell
source ~/.bashrc

# Notify the user
echo "Sublist3r and dirsearch have been installed and added to your PATH."
echo "You can now use them from anywhere in the terminal."

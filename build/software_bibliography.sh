#!/bin/bash

# Update the system's package list
sudo apt update && sudo apt upgrade -y

# Install core utilities and libraries

# Core utilities
sudo apt install -y coreutils  # GNU Core Utilities: Basic file, shell, and text manipulation tools
sudo apt install -y findutils  # Provides the 'find' command for searching files
sudo apt install -y grep       # Search for text patterns in files
sudo apt install -y sed        # Stream editor for text manipulation
sudo apt install -y awk        # Pattern scanning and text processing language

# Text processing and formatting tools
sudo apt install -y texlive     # LaTeX typesetting system for high-quality document preparation
sudo apt install -y texlive-latex-extra  # Additional LaTeX packages for advanced formatting
sudo apt install -y ghostscript # Interprets PostScript and PDF files
sudo apt install -y pandoc      # Universal document converter (e.g., Markdown to LaTeX/PDF)

# Command-line text editors
sudo apt install -y nano        # Simple text editor
sudo apt install -y vim         # Advanced text editor
sudo apt install -y emacs       # Extensible, customizable text editor

# Networking tools
sudo apt install -y curl        # Transfers data from or to a server (supports HTTP, FTP, etc.)
sudo apt install -y wget        # Non-interactive network downloader

# Version control
sudo apt install -y git         # Distributed version control system

# Software compilation tools
sudo apt install -y build-essential  # Essential tools for compiling software (gcc, make, etc.)
sudo apt install -y cmake            # Build system generator

# Programming languages
sudo apt install -y python3          # Python 3 programming language
sudo apt install -y python3-pip      # Python package manager (pip)
sudo apt install -y ruby             # Ruby programming language
sudo apt install -y perl             # Perl programming language
sudo apt install -y openjdk-11-jdk   # Java Development Kit (JDK)

# Miscellaneous tools
sudo apt install -y tree        # Displays directories in a tree-like format
sudo apt install -y htop        # Interactive process viewer
sudo apt install -y man-db      # Manual pages for Linux commands
sudo apt install -y tmux        # Terminal multiplexer
sudo apt install -y zip unzip   # Compress and decompress files
sudo apt install -y tar         # Archive files using tar format
sudo apt install -y lsof        # Lists open files

# Cleanup
sudo apt autoremove -y  # Remove unnecessary packages
sudo apt clean          # Clear package cache

# Final message
echo "Installation complete! Core libraries and tools have been installed."

# Notes:
# - The list includes tools commonly available on Debian-based systems like Ubuntu.
# - For Mac users, replace 'apt' with 'brew' for Homebrew package management.

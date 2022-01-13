set nocompatible
set wrap
filetype off
filetype plugin indent on
set number
syntax on
set laststatus=2

set mouse=a
set backspace=indent,eol,start
set showmode
set showcmd
set encoding=utf-8

" Searching
set hlsearch
set incsearch
set ignorecase
set smartcase


" Call the .vimrc.plug file
if filereadable(expand("~/.vimrc.plug"))
	source ~/.vimrc.plug
endif

nmap <C-t> :tabnext<Enter> 
"nmap <C-S-t> :tabprev<Enter>

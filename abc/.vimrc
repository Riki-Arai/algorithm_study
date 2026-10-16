"見た目関連
:syntax on "色をつける
:set number "行番号がわかるようにする
:set cursorline "カーソルがどの高さにあるかわかりやすくする
:set pumheight=10 "候補が10個出る
:set ruler " 右下に表示される行・列の番号を表示する
:set showmatch " 対応括弧をハイライト表示する
:set ambiwidth=double " □や○文字が崩れる問題を解決するが、コピペしにくなるのでコメントアウトウ
:set expandtab "タブの代わりに空白を使用する
:retab 4 "タブの間隔を4にする
:set shiftwidth=4 ">>を使用した時、指定した数値だけ空白を作る
:set tabstop=4 "タブを使用した時、指定した数値分の空白を作る
:hi Comment ctermfg=LightBlue "コメントアウトの色を変更

"検索関連
:set incsearch " インクリメンタルサーチ. １文字入力毎に検索を行う
:set ignorecase " 検索パターンに大文字小文字を区別しない
:set smartcase " ただし大文字も含めた検索の場合はその通りに検索する
:set hlsearch " 検索結果をハイライト

"移動関連
:set whichwrap=b,s,h,l,<,>,[,],~ "行頭で左へ移動しようとすると上の行末に移動できたりする
":set mouse=a "マウス操作を有効にする
:set autoindent
:set smartindent

"キーマップ
"nnoremap <silent> <CR> :call append(line('.'), '')<CR>
noremap <Space> <Esc>i<Space><Esc>
nnoremap vv viw
imap <C-d> <BS><BS><BS><BS>

"その他
:set noswapfile "スワップファイルを作成しない
:set history=1000 "コマンドの履歴を1000まで遡る
au BufNewFile,BufRead *.hql set filetype=hive expandtab " .hqlというファイルでHQLを記載している場合
au BufNewFile,BufRead *.q set filetype=hive expandtab " .qというファイルでHQLを記載している場合

nnoremap <silent> <C-w><C-w> :<C-u>call MyWincmdW()<CR>
nnoremap <silent> <C-w>w :<C-u>call MyWincmdW()<CR>
function! MyWincmdW()
  let pn = winnr()
  silent! wincmd w
  if pn == winnr()
    silent! b#
  endif
endfunction
; Script AutoHotkey para abrir o navegador e logar em uma URL especificada

; Caminho para o bloco de notas com a URL e credenciais
fullString := A_ScriptFullPath 
startPosition := 1 ; Posição inicial (1-indexed)
length := 31 ; Comprimento da substring a ser extraída

substring := SubStr(fullString, startPosition, length) "\ipstplink.txt"
FileRead, content, %substring%
; Divide o conteúdo em linhas
StringSplit, lines, content, `n


; Assume que a primeira linha é a URL, a segunda é o nome de usuário e a terceira é a senha
Loop, % lines0 {
    ; Assume que cada linha é uma URL
    url := lines%A_Index%
    Sleep 8000

    ; Abre o navegador e navega para a URL
    Run, firefox.exe %url%
    ; Alternativamente, você pode usar outro navegador como firefox.exe

    ; Espera a página carregar (ajuste o tempo conforme necessário)
    Sleep 8000
    ; Digita o nome de usuário (ajuste conforme o campo do formulário)

    Send, {Tab 2}
    Sleep, 2000
    Send, ****
    Send, {Tab}
    Sleep, 2000
    Send, *****
    Send, {Tab}
    Sleep, 2000
    Send, {Enter}
    Sleep, 5000
    Send, ^+i ; Ctrl+Shift+I é o atalho para abrir as DevTools no Chrome e Firefox
    Sleep, 2000
    Send, document.getElementsByClassName('nav-li')[5].click();
    Sleep, 2000
    Send, {Enter}
    Send, document.getElementsByClassName('ml1')[1].click() 
    Sleep, 2000
    Send, {Enter}
    Send, document.getElementsByClassName('grid-content-td-wrap')[16].click()
    Sleep, 2000
    Sleep, 5000
    Send, {Enter}
    Sleep, 2000
    concatenatedString := ""
    Sleep, 2000
    Send, {Enter}
    Send, let range = document.createRange()
    Send, {Enter}
    Sleep, 2000
    Send, {Enter}
    Sleep, 2000
    Send, let selection = window.getSelection()
    Send, {Enter}
    Sleep, 2000
    Send, selection.removeAllRanges()
    Send, {Enter}
    Sleep, 2000
    size := 28
    ; Loop através da lista usando o tamanho
    Loop, %size%
    {
        indexMinusOne := A_Index - 1
        Send, document.getElementsByClassName('content_detail')[ %indexMinusOne% ].click()
        Send, {Enter}
        Sleep, 2000
        Send, range.selectNodeContents(document.getElementsByClassName('widget-content msg-content-container')[7])
        Send, {Enter}
        Sleep, 2000
        Send, selection.addRange(range)
        Send, {Enter}
        Sleep, 5000
        Send, ^+i ; Ctrl+Shift+I é o atalho para abrir as DevTools no Chrome e Firefox
        Sleep, 2000
        Send, ^c ; Ctrl + C
        Sleep, 5000
        concatenatedString .= Clipboard
        Sleep, 2000
        Send, ^+i ; Ctrl+Shift+I é o atalho para abrir as DevTools no Chrome e Firefox
        Sleep, 5000
        ; A_Index é a variável de loop interna que começa de 1
    }
    ; ; Espera a cópia para a área de transferência completar
    Sleep, 1000

    ; ; Lê o conteúdo da área de transferência
    tableContent := concatenatedString

    ; Gera o nome do arquivo baseado na URL (substitui caracteres não permitidos por "_")
    fileName := StrReplace(url, "https://", "")
    fileName := StrReplace(fileName, "http://", "")
    fileName := RegExReplace(fileName, "[^A-Za-z0-9]", "_") ".txt"
        ; Obtém a data e a hora atual no formato AAAAMMDD_HHMMSS
    FormatTime, currentDateTime,, yyyyMMdd_HHmmss

    ; Acrescenta a data e a hora ao nome do arquivo
    fileName := fileName "_" currentDateTime ".txt"
    filePath := "\\Mac\Home\Documents\AutoHotkey\tplink\" fileName

    ; Salva o conteúdo copiado em um arquivo de texto
    FileAppend, %tableContent%, %filePath%
    ; Fecha a aba atual do navegador
    Sleep, 2000
   
    ; ; Espera um pouco antes de continuar para a próxima URL

}
; Process, Close, firefox.exe
MsgBox, Processo completo!
; Script AutoHotkey para abrir o navegador e logar em uma URL especificada

; Caminho para o bloco de notas com a URL e credenciais
fullString := A_ScriptFullPath 
startPosition := 1 ; Posição inicial (1-indexed)
length := 31 ; Comprimento da substring a ser extraída

substring := SubStr(fullString, startPosition, length) "\ipsintelbras.txt"
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
    Send, ^+i ; Ctrl+Shift+I é o atalho para abrir as DevTools no Chrome e Firefox

    ; Espera as Ferramentas de Desenvolvedor abrirem
    Sleep, 2000
    Send, document.getElementById('pn').value = "*****";
    Send, {Enter}
    Send, document.getElementById('pwd').value = "*****";
    Send, {Enter}
    Send, document.getElementById('btnLogin').click();
    Send, {Enter}
    Sleep, 2000
    ; doChange(2,'MibCounterRpm','portShow=1');
    ; Send, document.getElementById('port').value = porta;
    ; dosubmitRefresh();
    ; Espera as Ferramentas de Desenvolvedor abrirem
    Sleep, 2000
    Send, ^+i ; Ctrl+Shift+I é o atalho para abrir as DevTools no Chrome e Firefox

    Sleep, 2000
    Send, document.getElementById('ol5').click();
    Send, {Enter}
    Send, document.getElementById('ol8').click();
    Sleep, 200
    Send, {Enter}
    Send, document.getElementById('ulMenu_359_span').click();
    Sleep, 200
    Send, {Enter}
    Sleep, 2000
    Send, ^+i ; Ctrl+Shift+I é o atalho para abrir as DevTools no Chrome e Firefox
    Sleep, 2000
    Send, ^f
    Sleep, 500
    Send, Contadores porta
    Sleep, 500
    Send, {Enter}
    Sleep, 500
    Send, {Esc}
    Sleep, 500
    Send, ^a ; Ctrl + A
    Sleep, 150
    Send, ^c ; Ctrl + C

    ; Espera a cópia para a área de transferência completar
    Sleep, 1000

    ; Lê o conteúdo da área de transferência
    tableContent := Clipboard

    ; Gera o nome do arquivo baseado na URL (substitui caracteres não permitidos por "_")
    fileName := StrReplace(url, "https://", "")
    fileName := StrReplace(fileName, "http://", "")
    fileName := RegExReplace(fileName, "[^A-Za-z0-9]", "_") ".txt"
        ; Obtém a data e a hora atual no formato AAAAMMDD_HHMMSS
    FormatTime, currentDateTime,, yyyyMMdd_HHmmss

    ; Acrescenta a data e a hora ao nome do arquivo
    fileName := fileName "_" currentDateTime ".txt"
    filePath := "\\Mac\Home\Documents\AutoHotkey\intelbras\" fileName
    

    ; Salva o conteúdo copiado em um arquivo de texto
    FileAppend, %tableContent%, %filePath%
    ; Fecha a aba atual do navegador
    Sleep, 2000
   
    ; Espera um pouco antes de continuar para a próxima URL

}
Process, Close, firefox.exe
MsgBox, Processo completo!
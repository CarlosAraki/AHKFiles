; Script AutoHotkey para abrir o navegador e logar em uma URL especificada

; Caminho para o bloco de notas com a URL e credenciais
scriptDir := A_ScriptDir

; Executa os scripts um após o outro e aguarda a conclusão de cada um
RunWait, % scriptDir . "\crawler3com.ahk", , UseErrorLevel
if ErrorLevel
{
    MsgBox, Falha ao executar o script crawler3com.ahk
    ExitApp
}

RunWait, % scriptDir . "\crawlerDlink.ahk", , UseErrorLevel
if ErrorLevel
{
    MsgBox, Falha ao executar o script crawlerDlink.ahk
    ExitApp
}

RunWait, % scriptDir . "\crawlerTplink.ahk", , UseErrorLevel
if ErrorLevel
{
    MsgBox, Falha ao executar o script crawlerTplink.ahk
    ExitApp
}

; Descomente a linha abaixo se você deseja executar este script também
;RunWait, % scriptDir . "\crawlerIntelbras.ahk", , UseErrorLevel
;if ErrorLevel
;{
;    MsgBox, Falha ao executar o script crawlerIntelbras.ahk
;    ExitApp
;}

MsgBox, Processo Finalizado!

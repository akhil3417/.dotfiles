function piper_sgpt
    set prompt $argv
    set command "sgpt --top-p "0.01" --temperature "0.32" --no-cache --role jarvis --repl convi '$prompt' | tee /dev/tty | ~/gitclones/piper/piper --model ~/gitclones/piper/en_US-hfc_female-medium.onnx  --output-raw 2>/dev/null | aplay -r 22050 -f S16_LE -t raw - 2>/dev/null"
    eval $command
end

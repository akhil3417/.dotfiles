function piper_sgpt
    set prompt $argv
    set command "sgpt --role chat '$prompt' | ~/gitclones/piper/piper --model ~/gitclones/piper/en_US-hfc_female-medium.onnx  --output-raw | aplay -r 22050 -f S16_LE -t raw -"
    eval $command
end

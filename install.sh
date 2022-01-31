#!/usr/bin/bash

git submodule update --init --recursive
pip install -r requirements.txt
rm -R bin
mkdir bin
wget https://github.com/FlUxIuS/V2Gdecoder/releases/download/v1/V2Gdecoder.jar --directory-prefix=bin
rm V2GDecoder_default_run.sh
tee -a V2GDecoder_default_run.sh << END
#!/usr/bin/bash

java -jar bin/V2Gdecoder.jar -w
END
chmod +x V2GDecoder_default_run.sh
ln -s thirdparty/V2Gdecoder/schemas schemas

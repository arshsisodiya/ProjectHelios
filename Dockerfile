FROM frost2k5/dragonheart:master

RUN mkdir /Fizilion && chmod 777 /Fizilion && git clone https://github.com/arshsisodiya/ProjectHelios -b test /Fizilion
ENV PATH="/Fizilion/bin:$PATH"
WORKDIR /Fizilion

CMD ["python3","-m","userbot"]

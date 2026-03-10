def run():


    # input file jisme sab links hain
    input_file = "Paste_links.txt"
    
    # output file jisme sirf /vdp/ links save honge
    output_file = "vdp_links.txt"
    
    # output file ko clean karo
    open(output_file, "w").close()
    
    # input file read karo
    with open(input_file, "r", encoding="utf-8") as file:
        links = file.readlines()
    
    # filter aur save
    with open(output_file, "a", encoding="utf-8") as file:
        for link in links:
            link = link.strip()
    
            if "/vdp/" in link:
                file.write(link + "\n")
    
    print("Done ✅  /vdp/ links save ho gaye.")
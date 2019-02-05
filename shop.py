import argparse
import PIL
# this is My 1.4.7 project
#My name is Caden Kline 
#there are 2 options this program can do 
#invert the colors of a picture or paste 1 picture on top of another
def invert_colors(image):
    pix = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.mode == "RGB":
                pix[x,y] = ((pix[x,y][0]+155) % 255,(pix[x,y][1]+155) % 255,(pix[x,y][2]+155) % 255)
            else:
                pix[x,y] = ((pix[x,y][0]+155) % 255,(pix[x,y][1]+155) % 255,(pix[x,y][2]+155) % 255,pix[x,y][3])
    return image
def paste(picture, picture2):
    picture.paste(picture2,None) 
    return picture
    
def main():
    # this is the code that gets runs when the program does
    #It reads the inputs in and parses them
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="choose photo mode [invert, paste]")
    parser.add_argument("picture", help="file name of picture")
    parser.add_argument("--picture2", help="second picture for pasting")
    args = parser.parse_args()
    #these arguments are then used to determine what action is done
    picture = PIL.Image.open(args.picture)
    if args.mode == 'invert':
        #lets see an example of invert
        #You just pick the mode and the picture
        picture = invert_colors(picture)
    elif args.mode == "paste":
        picture2 = PIL.Image.open(args.picture2)
        picture = paste(picture,picture2)
    else:
        print "pick correct mode"
        exit()
    picture.save("a.png")
        
if __name__ == '__main__':
    main()
def invert_colors(image):
    pix = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.mode == "RGB":
                pix[x,y] = ((pix[x,y][0]+155) % 255,(pix[x,y][1]+155) % 255,(pix[x,y][2]+155) % 255)
            else:
                pix[x,y] = ((pix[x,y][0]+155) % 255,(pix[x,y][1]+155) % 255,(pix[x,y][2]+155) % 255,pix[x,y][3])
    return image
def paste(picture, picture2):
    picture.paste(picture2,None)
    

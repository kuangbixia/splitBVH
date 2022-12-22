def main():
    path = "/home/kbx/Datasets/HDM05/volleyball/AMC/"
    originalBVH = "list.bvh"
    newBVH = "serving.bvh"

    r = open(path+originalBVH, "r")
    lines = r.readlines()
    firstFrame = 1830
    lastFrame = 2023
    w = open(path+newBVH, "w")
    i = 0
    for line in lines:
        if line[:6] == "Frames":
            w.write("Frames: {}\n".format(lastFrame - firstFrame + 1))
            continue
        if line[:10] == "Frame Time":
            w.write(line)
            i += 1
            continue
        if i == 0:
            w.write(line)
        elif i > 0:
            if i >= firstFrame and i <= lastFrame:
                w.write(line)
            i += 1
            if i > lastFrame:
                break


if __name__=="__main__":
    main()
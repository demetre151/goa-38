import fs from "fs";
const kidsHelp = (num) => {

    const handleFileCreate = (x, flName, content) => {
        const filePath = `./${x}/${flName}`
        try {
            fs.writeFileSync(filePath, content);
            console.log("File created successfully.");
        } catch (err) {
            console.error("Error creating file:", err);
        }
    }
    const handleDirMake = (dirPath) => {
        fs.mkdir(dirPath, { recursive: true }, (err) => {
            if (err) {
                console.error("Error creating directory:", err);
                return;
            }
        })
    }
    for (let i = 31; i < num + 1; i++) {
        let fileNum = String(i).padStart(2, "0")
        handleDirMake(`level ${fileNum}`)
        handleDirMake(`level ${fileNum}/classwork`)
        handleDirMake(`level ${fileNum}/homework`)
        handleFileCreate(`level ${fileNum}/homework`, "homework.txt", "# No homework")
        handleFileCreate(`level ${fileNum}/classwork`, "classwork.txt", "# No classwork")

    }
}
kidsHelp(31)

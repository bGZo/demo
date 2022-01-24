// via https://turingplanet.org/2020/07/15/javascript_hw_answer/
// thx for https://turingplanet.org/javascript
function strangeRange(a, b){
    while(true){
        var num1=window.prompt("Enter Num1:"); //FIXME:get user input
        var num2=window.prompt("Enter Num2:");

        if(num1>num2) break;
        for(var i=num1;i<=num2;i++){
            if(i&1==1) console.log(i);
        }
    }
}

function plusTwoArrayNum(array1, array2){
    var targetArray=[];
    for(var i=0;i<array1.length;i++){
        targetArray.join(array1[i]+array2[i]);
    }
    return targetArray;
}

function objectCar(brand){ //NOTE:object also a object
    this.brand=brand;
    this.model="xxx";
    this.year=0;

    this.setModel=function(model){this.brand.model=model;}
    this.setYear=function(year){this.brand.year=year;}
    this.getInfo=function(){
        console.log("Brand: Branch:$(this.brand), Model:$(this.model), Year: $(this.year)");
    }
}




const fs=require('fs'); //???????
var express=require('express');
const bodyParser = require('body-parser');
var app=express();
app.use(express.json);

app.get('/json_file',(req, res)=>{
    try{
        let data=fs.readFileSync(`${__dirname}/${req.query.name}.json`)
        res.json(JSON.parse(data));
    }
    catch(err){
        console.error(err);
        res.send({'error':err.toString()});
    }
});

app.post('/json_file', (req, res)=>{
    try{
        const fileName=__dirname+'/'+req.query.name+'.json';
        bodyData=req.body;
        fs.open(fileName, 'r', (err, fd)=>{
            if(err){
                fs.writeFile(fileName, JSON.stringify(bodyData),(err)=>{if(err) console.log(err);});
            }else{
                let fileContent=JSON.parse(fs.readFileSync(fileName, 'utf-8'));
                Object.keys(bodyData).forEach((key)=>{fileContent[key]=bodyData[key];});
                fs.writeFileSync(fileName, JSON.stringify(fileContent));
            }
        })
        res.send({'success':'File successfully updated.'})
    }catch(err){
        console.log(err);
        res.send({'error':'Update json file failed.'})
    }
})


app.delete('/json_file', (req, res)=>{
    try{
        fs.unlinkSync(__dirname+'/'+req.query.name+'.json');
        res.send({'success':'File deleted.'})
    }catch(err){
        console.log(err);
        res.send({'error':'Delete file failed.'})
    }
});

const port=8080;
app.listen(port, ()=>{
    console.log(`Server listening @ http://127.0.0.1:${port}`)
})


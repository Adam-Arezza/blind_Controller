const express = require('express')
const cors = require('cors')
const bodyParser = require('body-parser')
const {PythonShell} = require('python-shell')
const app = express()

app.use(express.static('../dist/'))
app.use(cors())
app.use(bodyParser.json())
app.use(bodyParser.text())


app.post('/blinds-manual', function(req,res){
    console.log(req.body)
    PythonShell.run('./py_scripts/manualBlinds.py',{args:[JSON.stringify(req.body)]}, function(err,results){
        if(err){
            console.log(err)
            res.send("Error connecting to blinds")
        }
        if(results){
            var response = {}
            response.pyRes = results
            res.send(response.pyRes)
        }
    })
})

app.post('/blinds-auto', function(req,res){
    var request = req.body
    var time = request.setTime.split(':')
    var min = time[1]
    var hour = time[0]
    // console.log(request)
    console.log(min, hour)
    if(request.setTime){
        require('crontab').load(function(err,crontab){
            var jobs = crontab.jobs()
            for(job in jobs){
                console.log(jobs[job])
                console.log(jobs[job].comment())
                if(jobs[job].comment() == 'testing node cron'){
                    crontab.remove(jobs[job])
                    crontab.save(function(err, crontab){
                        if(err){
                            console.log(err)
                        }
                    })
                }
            }
            var job = crontab.create('python3 Desktop/test.py', min + ' ' + hour + ' * * *','testing node cron')
            crontab.save(function(err, crontab){
                if(err){
                    console.log(err)
                }
            })
        })
    }
    res.send("created cron job for blinds to open at: " )
})

app.listen(3000)
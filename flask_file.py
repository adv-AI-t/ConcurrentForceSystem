from flask import Flask, request
import numpy as np
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def calc():
    if request.method == 'POST':
        w = float(request.form['weight'])

        t1 = float(request.form['t1'])
        t2 = float(request.form['t2'])
        t3 = float(request.form['t3'])

        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        z1 = float(request.form['z1'])

        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])
        z2 = float(request.form['z2'])

        x3 = float(request.form['x3'])
        y3 = float(request.form['y3'])
        z3 = float(request.form['z3'])

        xp = float(request.form['xp'])
        yp = float(request.form['yp'])
        zp = float(request.form['zp'])

        mag1 = ((x1 - xp) ** 2 + (y1 - yp) ** 2 + (z1 - zp) ** 2) ** 0.5
        mag2 = ((x2 - xp) ** 2 + (y2 - yp) ** 2 + (z2 - zp) ** 2) ** 0.5
        mag3 = ((x3 - xp) ** 2 + (y3 - yp) ** 2 + (z3 - zp) ** 2) ** 0.5

        A = np.array([[(x1 - xp) / mag1, (x2 - xp) / mag2, (x3 - xp) / mag3],
                      [(y1 - yp) / mag1, (y2 - yp) / mag2, (y3 - yp) / mag3],
                      [(z1 - zp) / mag1, (z2 - zp) / mag2, (z3 - zp) / mag3]])
        B = np.array([0, 0, -w])

        C = np.linalg.solve(A, B)

        err1 = abs((t1 - C[0])/C[0])*100
        err2 = abs((t2 - C[1])/C[1])*100
        err3 = abs((t3 - C[2])/C[2])*100

        return f'''
                    <html>
                    <body>
                    <b>Analytical values:</b>
                    <br>
                    T1 = {C[0]} N
                    <br>
                    T2 = {C[1]} N
                    <br>
                    T3 = {C[2]} N
                    <br><br>
                    Percentage errors in readings: 
                    <br><br>
                    Error in T1 = {err1} %
                    <br>
                    Error in T2 = {err2} %
                    <br>
                    Error in T3 = {err3} %
                    </body>
                    </html>
        '''
    else:
        return '''
        <form method = "post">
        <head>
        <title>
        Concurrent Force System in Space
        </title>
        </head>
        <body>
        <i>Consider the weight acting along positive Z axis</i>
        <br>
        <table>
        <tr>
        <td>
        <label for = "weight">Enter weight of body in Newton:</label>
        </td>
        <td>
        <input type="number" id="weight" name="weight" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "t1">Enter experimental value of tension in string 1:</label>
        </td>
        <td>
        <input type="number" id="t1" name="t1" step = "0.001" required>
        </td>
        <td>
        <label for = "t2">Enter experimental value of tension in string 2:</label>
        </td>
        <td>
        <input type="number" id="t2" name="t2" step = "0.001" required>
        </td>
        <td>
        <label for = "t3">Enter experimental value of tension in string 3:</label>
        </td>
        <td>
        <input type="number" id="t3" name="t3" step = "0.001" required>
        </td>
        </tr>
        </table>
        <br><br>
        
        Enter co-ordinates of point 1:
        <br>
        <table>
        <tr>
        <td>
        <label for = "x1">x co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="x1" name="x1" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "y1">y co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="x2" name="x2" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "z1">z co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="x3" name="x3" required>
        </td>
        </tr>
        </table>
        <br>
        
        Enter co-ordinates of point 2:
        <table>
        <tr>
        <td>
        <label for = "x2">x co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="x2" name="x2" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "y2">y co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="y2" name="y2" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "z2">z co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="z2" name="z2" required>
        </td>
        </tr>
        </table>
        
        Enter co-ordinates of point 3:
        <table>
        <tr>
        <td>
        <label for = "x3">x co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="x3" name="x3" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "y3">y co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="y3" name="y3" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "z3">z co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="z3" name="z3" required>
        </td>
        </tr>
        </table>
        
        Enter co-ordinates of point P:
        <br>
        <table>
        <tr>
        <td>
        <label for = "xp">x co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="xp" name="xp" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "yp">y co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="yp" name="yp" required>
        </td>
        </tr>
        <tr>
        <td>
        <label for = "zp">z co-ordinate:</label>
        </td>
        <td>
        <input type="number" id="zp" name="zp" required>
        </td>
        </tr>
        </table>
        <input type="submit" value="Check result">
        </form>
        
        <br><br>
            <font style="font-family:Arial">
            <b>Guided by:</b><br><br>
            Prof. E. M. Reddy<br>
            <i>HoD First Year Engineering Department, Pune Institute of Computer Technology</i><br><br>
            <b>A Flask web application by:</b><br><br>
            Advait Joshi<br>
            <i>CE Undergrad at Pune Institute of Computer Technology</i><br>
            Email: joshiadvait07@gmail.com<br>
            <a href="https://www.linkedin.com/in/advait-joshi-b61410256">Click to view LinkedIn profile</a>
        </body>
        '''
if __name__ == '__main__':
    app.run(port="5005")
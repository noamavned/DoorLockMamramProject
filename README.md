
# מנעול חכם לדלת

*פרויקט זה נוצר בשביל ממר"ם האקת'ון*
המנעול הוא מנעול חכם בעל קורא כרטיסים השמורים בפרויקט עצמו
ניתן לשלוט במנעול דרך תוכנת צ'אט הנקראת "דיסקורד" עם מספר פונקציות מיוחדות

#

:כאשר המשתמש ניגש אל המנעול הוא יכול להשתמש בשני אפשרויות
* בעזרת כרטיס רשום
* בעזרת "דיסקורד" דרך מכשיר חכם

# שימוש בעזרת כרטיס

בהנחה הראשונה של הכרטיס על קורא הכרטיסים יושמע צפצוף קצר והמנעול יפתח
לנעילת המנעול יש להניח את הכרטיס על קורא הכרטיסים שנית וכמו בפתיחת המנעול יושמע צפצוף קצר

כאשר מונח כרטיס בעל אותו תדר כמו קורא הכרטיסים יושמעו שלושה צפצופים רצופים ובצפצוף השלישי לא תהיה אפשרות לניסיון כניסה במשך כמה שניות (לצורך ההדגמה בלבד. צריך לשנות בזמן אמת לכרבע שעה) ותשלח התרעה לרובוט הרשום במכשיר עם תמונה של ניסיון הכניסה

# שימוש בעזרת מכשיר חכם

כאשר המשתמש רוצה להשתמש במכשיר החכם שלו (כל מכשיר שיכול להריץ את התכנה "דיסקורד") הוא יכול להיכנס לסרבר שהוא יצר עם הבוט המחובר
**פקודות אלו צורכות סיסמא**

# סרטוט חשמלי

<p align="right">
  <img src="https://github.com/noamavned/DoorLockMamramProject/blob/main/images_not_related/circuit.jpg" width="200" title="hi">
</p>

# פקודות

<p align="right">
    <table>
        <thead>
            <tr>
                <th>Command</th>
                <th>Description</th>
                <th>Password needed</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>lock</td>
                <td style="text-align:right">נועל את המנעול</td>
                <td style="text-align:center">✔</td>
            </tr>
            <tr>
                <td>unlock</td>
                <td style="text-align:right">פותח את המנעול</td>
                <td style="text-align:center">✔</td>
            </tr>
            <tr>
                <td>state</td>
                <td style="text-align:right">מחזיר הודעה האומרת אם המנעול פתוח או נעול</td>
                <td style="text-align:center">✔</td>
            </tr>
            <tr>
                <td>show_trys</td>
                <td style="text-align:right">מחזיר הודעה האומרת כמה ניסיונות שגויים נשארו עד לנעילה של המנעול</td>
                <td style="text-align:center"></td>
            </tr>
            <tr>
                <td>send_pic</td>
                <td style="text-align:right">שולח תמונה מהמצלמה</td>
                <td style="text-align:center"></td>
            </tr>
            <tr>
                <td>beep</td>
                <td style="text-align:right">מפעיל צפירה ארוכה מהמנעול</td>
                <td style="text-align:center">✔</td>
            </tr>
            <tr>
                <td>reset_trys</td>
                <td style="text-align:right">מאפס את הנסיונות השגויים לנעילה של המנעול</td>
                <td style="text-align:center">✔</td>
            </tr>
            <tr>
                <td>ping</td>
                <td style="text-align:right">פקודה המחזירה את הזמן הגבה של הבוט לשרת</td>
                <td style="text-align:center">✔</td>
            </tr>
            <tr>
                <td>reboot</td>
                <td style="text-align:right">מאתחל את המכשיר</td>
                <td style="text-align:center">✔</td>
            </tr>
            <tr>
                <td>set_channel</td>
                <td style="text-align:right">מגדיר את הערוץ אליו נשלחות ההתרעות </br><strong>כאשר לא מוגדר ערוץ לא ישלחו הודעות</strong></td>
                <td style="text-align:center">✔</td>
            </tr>
        </tbody>
    </table>
</p>








</br></br>
## Hey there, I'm Noam!

- 🌟 [Github](https://github.com/noamavned): Check out my latest projects and contributions!
- 💬 [Discord](https://discord.com/): You can find me as CHEF#4136. Let's chat!
- 📸 [Instagram](https://www.instagram.com/noam_avned/): Follow me on Instagram to see some of my latest photos and adventures!

<p align="center">
  <img src="https://github.com/noamavned/DoorLockMamramProject/blob/main/images_not_related/onlinelogo.jpg" width="200" title="hi">
</p>

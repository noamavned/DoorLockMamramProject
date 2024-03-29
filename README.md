
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

# סרטוט חשמל

<p align="right">
  <img src="https://github.com/noamavned/DoorLockMamramProject/blob/main/images_not_related/circuit.jpg" width="500" title="hi">
</p>

# פקודות

| Command |     Description     | Password needed |
|---|---:|:-:|
| lock | נועל את המנעול | ✔ |
| unlock | פותח את המנעול | ✔ |
| state | מחזיר הודעה האומרת אם המנעול פתוח או נעול | ✔ |
| show_trys | מחזיר הודעה האומרת כמה ניסיונות שגויים נשארו עד לנעילה של המנעול |  |
| send_pic | שולח תמונה מהמצלמה |  |
| beep | מפעיל צפירה ארוכה מהמנעול | ✔ |
| reset_trys | מאפס את הנסיונות השגויים לנעילה של המנעול | ✔ |
| ping | פקודה המחזירה את הזמן הגבה של הבוט לשרת | ✔ |
| reboot | מאתחל את המכשיר | ✔ |
| set_channel | מגדיר את הערוץ אליו נשלחות ההתרעות </br> **כאשר לא מוגדר ערוץ לא ישלחו הודעות** | ✔ |







</br></br>
## Hey there, I'm Noam!

- 🌟 [Github](https://github.com/noamavned): Check out my latest projects and contributions!
- 💬 [Discord](https://discord.com/): You can find me as chef4136. Let's chat!
- 📸 [Instagram](https://www.instagram.com/noam_avned/): Follow me on Instagram to see some of my latest photos and adventures!

<p align="center">
  <img src="https://github.com/noamavned/DoorLockMamramProject/blob/main/images_not_related/onlinelogo.jpg" width="200" title="hi">
</p>

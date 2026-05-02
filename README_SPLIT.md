# Part 2: levels 3-4

This archive is intended for the second commit after part 1.

Added:
- Separate Currency model.
- Currencies are added by admin only.
- Website form uses dropdown with available currencies.
- API endpoint: /api/rates/today/.

If applying after part 1, run:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

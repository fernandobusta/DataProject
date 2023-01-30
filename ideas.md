
# Ideas

## Database and APIs
- Save searches in the db
- When doing a search, if the search has already been done, get the data from the database instead of calling the API to run another search
	- This saves money, as keeping something in the db is less expensive constantly running API calls
	- Maybe delete after a certain time, if too much space is occupied
	- If the new search has different values, but the same location, only search for the new values and get the rest of the parameters from the db

# ivi_api_autotests

# Path to /src/tests

# TEST-CASES:
# 1. Get all heroes info
#   Steps:
#   1. curl 'http://rest.test.ivi.ru/v2/characters' -u username:password
#   Expected result:
#   200 Ok, validation schema of body response ok
#

# 2. Get any hero info
#   Steps:
#   1. curl 'http://rest.test.ivi.ru/v2/characters' -u username:password
#   2. Choose random hero with NAME
#   3. curl 'http://rest.test.ivi.ru/v2/character?name=NAME' -u username:password
#   Expected result:
#   200 Ok, validation schema of body response ok, info from (1) and (2) matches
#

# 3. Create hero
#   Steps:
#   1. Set name, universe, education, weight, height, identity as valid data
#   2. curl -X POST -H 'Content-type: application/json' 
#      -u username:password
#      -d '{"name": "Hawkeye", "universe": "Marvel Universe", 
#           "education": "High school (unfinished)", "weight": 104, 
#           "height": 1.90, "identity": "Publicly known"}'
#           'http://rest.test.ivi.ru/v2/character'
#   3. Check that hero created
#   Expected result:
#   200 Ok, validation schema of body response ok
#

# 3. Create 501 heroes
#   Steps:
#   1. Count how many heroes are created
#   2. Set name, universe, education, weight, height, identity as valid data
#   3. curl -X POST -H 'Content-type: application/json' 
#      -u username:password
#      -d '{"name": "Hawkeye", "universe": "Marvel Universe", 
#           "education": "High school (unfinished)", "weight": 104, 
#           "height": 1.90, "identity": "Publicly known"}'
#           'http://rest.test.ivi.ru/v2/character'
#   3. Repeat second step for (501 - count of created hero) times
#   4. Create 501-st hero
#   Expected result:
#   400 Bad Request, error text in the body response ok
#

# 3. Create hero with invalid data
#   Steps:
#   1. Set universe, education, weight, height, identity as valid data
#   2. Set invalid data for name
#   3. curl -X POST -H 'Content-type: application/json' 
#      -u username:password
#      -d '{"name": "Hawkeye", "universe": "Marvel Universe", 
#           "education": "High school (unfinished)", "weight": 104, 
#           "height": 1.90, "identity": "Publicly known"}'
#           'http://rest.test.ivi.ru/v2/character'
#   Expected result:
#   400 Bad Request, error text in the body response ok
#

# 4. Update hero information
#   Steps:
#   1. Find random hero with NAME
#   2. Set universe, education, weight, height, identity as valid data
#   3. curl -X PUT -H 'Content-type: application/json' 
#      -u username:password
#      -d '{"name": "Hawkeye", "universe": "Marvel Universe", 
#           "education": "High school (unfinished)", "weight": 104, 
#           "height": 1.90, "identity": "Publicly known"}'
#           'http://rest.test.ivi.ru/v2/character?name=NAME'
#   4. Check that hero is updated
#   Expected result:
#   200 Ok, validation schema of body response ok
#

# 5. Delete hero
#   Steps:
#   1. Create new hero with NAME
#   2. Delete created hero
#   3. curl -X DELETE 'http://rest.test.ivi.ru/v2/character?name=NAME' -u username:password
#   4. Check that hero is deleted
#   Expected result:
#   200 Ok, validation schema of body response ok
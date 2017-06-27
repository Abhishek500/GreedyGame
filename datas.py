from datetime import datetime


def unix_time_millis(dt):
    return int(dt.strftime("%s")) 
def str2time(s):
    parts = s.split('.')
    dt = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
    return unix_time_millis(dt.replace(microsecond=int(parts[1])))




def session_time(arr): 
  sessions=[]
  n=len(arr)
  i=0
  end_time=0
  wrong_data_count=0
  merged_session_count=0
  while(i<n):
    if(arr[i][0]=='ggstart'):
      while(i<n and arr[i][0]=='ggstart'):
        i+=1
        wrong_data_count+=1
      if (i>n-1):
        break 
      session_length=arr[i][1]-arr[i-1][1]
      
      if (session_length>=1 and (end_time==0 or arr[i-1][1]-end_time)>30):
        sessions.append(session_length)
      elif len(sessions)==0 and session_length>=1:
        sessions.append(session_length)
      elif (session_length>=1):
        sessions[-1]+=session_length
        merged_session_count+=1
      
      end_time=arr[i][1]
      i+=1
    else:
      while(i < n and arr[i][0]=='ggstop' ):
        i+=1
        wrong_data_count+=1
       
  return sessions,wrong_data_count,merged_session_count
		
lines = tuple(open('ggevent.log', 'r'))
import json
arr=[]
for line in lines:
  arr.append(json.loads(line))
data={}
for a in arr:
  game_id=a['bottle']['game_id']
  if game_id in data :
   	data[game_id].append([a['post']['event'],a['post']['ts'],a['headers']['ai5'],a['headers']['sdkv'],a['bottle']['timestamp']])
  else :
   	data[game_id]=[[a['post']['event'],a['post']['ts'],a['headers']['ai5'],a['headers']['sdkv'],a['bottle']['timestamp']]]
sessions=[]

for d in data:
  users={}
  session_count=0
  valid_session_count=0
  valid_session_length=0
  for sess in data[d]:
    user_id=sess[2]
    if user_id in users:
      users[user_id].append([sess[0],str2time(sess[4]),sess[1],sess[3]])
    else :
      users[user_id]=[[sess[0],str2time(sess[4]),sess[1],sess[3]]]
  user_sessions=[]
  wrong_data_count=0
  merged_session_count=0
  for id in users:
    user_sess,wrong_data,merged_session=session_time(users[id])
    user_sessions+=user_sess
    wrong_data_count+=wrong_data
    merged_session_count+=merged_session
  session_count+=len(user_sessions)
  if session_count+merged_session_count != 0:
    adjusted_session_count=session_count+wrong_data_count*(session_count/(session_count+merged_session_count))
  else:
    adjusted_session_count=0
  valid_session=[i for i in user_sessions if i >60] 
  valid_session_count=len(valid_session)
  if (session_count != 0):
    adjusted_valid_session_count=adjusted_session_count*valid_session_count/session_count
  else:
    adjusted_valid_session_count=0
  valid_session_length=sum(valid_session)
  avg_session_length=0 if (valid_session_count==0) else valid_session_length/valid_session_count
  sessions.append([d,session_count,valid_session_count,int(adjusted_session_count),int(adjusted_valid_session_count),avg_session_length])
sessions.sort()
print(session)

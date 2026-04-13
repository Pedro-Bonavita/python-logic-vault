#DATABASE
raw_playlist = ["CLINT-EASTWOOD_GORILLAZ","JAMMING_BOB-MARLEY"]

print("=====INGESTION PROCESS STARTING=====")
print("Follow the instructions to add songs")
# 1. Extraction & Transformation
while True:
    song = input("Enter song name(or type 'exit'): ")

    if song.lower() =='exit':
      
      break
    else:
       artist = input("Enter artist name: ")

       song_cleaned = song.strip().upper()
    artist_cleaned = artist.strip().upper()

entry = f"{artist_cleaned}_{song_cleaned}"
raw_playlist.append(entry)
print(f"{entry} ingested.")

  
# Data transformation


# 2. Loading & reporting
print("\n--- ETL REPORT: FINAL PLAYLIST ---")

for i in range(len(raw_playlist)):
  print(f"Record {i+1}: {raw_playlist[i]}")
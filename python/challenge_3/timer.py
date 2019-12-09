three1 = __import__('3_1')
import time

start_time = time.time()
answer = three1.main()
print("--- %s seconds ---" % (time.time() - start_time))
print(answer)

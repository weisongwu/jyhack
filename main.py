import os
import jyhack_battle
import jyhack_event
import jyhack_r1
import jyhack_scene
import jyhack_smp
def main():

    os.makedirs("./data_export", exist_ok=True)
    os.makedirs("./img_export", exist_ok=True)
    
    jyhack_battle.main()
    jyhack_event.main()
    jyhack_r1.main()
    jyhack_scene.main()
    jyhack_smp.main()
if __name__ == "__main__":
    main()
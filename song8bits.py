#include <Tone32.h>

#define BUZZER_PIN 14
#define BUZZER_CHANNEL 0

const int melody[] = {262, 262, 294, 294, 330, 330, 294, 0,
                      247, 247, 220, 220, 196, 196, 220, 0,
                      294, 294, 247, 247, 220, 220, 196, 0,
                      262, 262, 294, 294, 330, 330, 294, 0,
                      247, 247, 220, 220, 196, 196, 220, 0};

const int noteDurations[] = {500, 500, 500, 500, 500, 500, 1000, 500,
                              500, 500, 500, 500, 500, 500, 1000, 500,
                              500, 500, 500, 500, 500, 500, 1000, 500,
                              500, 500, 500, 500, 500, 500, 1000, 500};

int melodyLength = sizeof(melody) / sizeof(melody[0]);

void setup() {
  Serial.begin(115200);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  for (int i = 0; i < melodyLength; i++) {
    int frequency = melody[i];
    int duration = noteDurations[i];

    if (frequency > 0) {
      // เล่นโน้ตด้วย Tone32
      tone(BUZZER_PIN, frequency, duration, BUZZER_CHANNEL);
      delay(duration);  // รอให้โน้ตเล่นจบก่อนเล่นตัวต่อไป
    } else {
      delay(duration);  // โน้ตพัก (ไม่มีเสียง)
    }
  }
  
  Serial.println("เพลงเล่นจบแล้ว รอ 2 วินาทีก่อนเล่นใหม่");
  delay(2000);  // เว้นช่วงระหว่างเพลง
}

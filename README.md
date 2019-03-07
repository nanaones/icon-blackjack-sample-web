# BLACK JACK 
ICON SCORE인 Black Jack 에 GUI를 추가하여, 사용자가 접근하기 쉽게 한다.  
ICON SCORE의 Sample로 활용한다.

## 개발환경
-   Python3.6
-   django 2.0.1
-   iconsdk

## Page
### 작성된 페이지
    
a. Ori  
    ``` /Ori```  
  1. Template의 Original Page 
  
b. Room  
    ```/room```   
  1. 현재 존재하는 게임룸 출력
  2. Testnet에 배포되어있는 Sample Game SCORE
  
      ``` SCORE address : cx89245b4a663f2062a9fe52a219c44c281e1d6c36 ``` 
  
  3. 2의 SCORE에서 show_game_room_list 의 icx_call 결과 
  4. Click 으로 세부내용 확인
  5. 세부내용 페이지에서 진행 가능한 게임일 경우, Join 기능[미구현]

c. Sample  
```/Sample```  
  1. ICONex Wallet에서 제공한 Sample 을 구현
  2. Transaction 전송 기능 구현[미구현]

d. Make Game Room

``` /make ```
    1. Game Room 을 만든다.[미구현]

e. Check Token Balance

``` /balance ```

  1. ICONex 를 통해, BlackJack Game에 있는 BalanceOf(msg.sender) 메서드를 호출하여, 현재 사용자의 Balance를 조회한다. 
    
f. Mint Token

``` /mint ```

  1. 사용자가 원하는 만큼의 Token을 mint 한다.
  2. BlackJack Game에 있는 mintToken() 메서드를 통해 Token을 Mint 한다.  
  3. Sign에는 ICONex를 활용한다.
    
1. Sample Game SCORE의 create_room 메서드를 실행하여 게임룸을 만드는 페이지
2. create_room 메서드를 icx_SendTransaction 을 통해서 gameroom 을 생성한다. [미구현]

## 설치하기

```$ git clone  https://github.com/nanaones/TBD_Web_1```

```$ python manage runserver 0.0.0.0:8000```


## TBD


### project 구성  


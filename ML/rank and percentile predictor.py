from model1 import prediction
from model2 import predict_rank

def main():
    print("JEE percentile & rank predictor")
    try:
        marks=float(input("Enter marks: "))
        year=int(input("Enter year: "))

        if not (0<=marks<=300):
            print("marks must be between 0 and 300")
            return
        percentile = prediction(marks)
        rank=predict_rank(percentile,year)

        print("\n PREDICTED RESULT:")
        print(f"Marks:{marks}")
        print(f"Predicted percentile:{round(percentile,4)}")
        print(f"Predicted rank:{rank}")

    except Exception as e:
        print("error", e)

if __name__ == "__main__":
    main()
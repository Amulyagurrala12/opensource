X = int(input().strip())
amount_after_coupon1 = 0.90 * X
amount_after_coupon2 = X - 100
final_amount = min(amount_after_coupon1, amount_after_coupon2)
print(int(final_amount))

def count_primes(limit: int) -> int:
    count: int = 0
    for candidate_int in range(limit):
        if (candidate_int > 1):
            for factor in range(2, candidate_int):
                if candidate_int % factor == 0:
                    break
            else:
                count += 1
    return count


count_primes(100000)

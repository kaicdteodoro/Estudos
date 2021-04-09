<?php

// Complete the jumpingOnClouds function below.
/* Exercício do site Hacker Hank
A exibição no site está sendo feita por fopen,
não sei ainda implementar sozinho isso,
então fiz a entrada direto na variável, só para fer se funciona direitinho*/
$c = preg_split("/ /", "0 0 1 0 0 1 0");

function jumpingOnClouds($c)
{
    $cont = 0;
    $i = 0;
    for ($i = 0; $i <= count($c) - 1; $i++) {
        if ($i + 1 <= (count($c) - 1)) {
            if ($c[$i + 1] === 0) {
                if ($i + 2 <= (count($c) - 1)) {
                    if ($c[$i + 2] === 0) {
                        $i++;
                    }
                }
                $cont++;
            } else {
                $cont++;
                $i++;
            }
        }
    }
    return $cont;
}

echo "Result: " . jumpingOnClouds($c);
